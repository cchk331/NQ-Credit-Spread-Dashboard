#!/bin/bash
# ============================================================
# tunnel_start.sh
# Run on YOUR LOCAL MACHINE to start the IB Gateway tunnel
# to your GitHub Codespace.
# ============================================================

set -e

# Check gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo "ERROR: GitHub CLI not installed."
    echo "Install: https://cli.github.com/"
    exit 1
fi

# List available codespaces
echo "Available Codespaces:"
gh codespace list

echo ""
read -p "Enter your codespace name: " CODESPACE_NAME

# Check Docker container is running
if ! docker ps | grep -q "ib-gateway"; then
    echo "WARNING: IB Gateway Docker container not running!"
    echo "Start it first: cd ib-gateway && docker-compose up -d"
    exit 1
fi

echo "Starting tunnel: Codespace:4002 → localhost:4002"
echo "Keep this terminal open (or Ctrl+C to stop)"
echo ""

# Use tmux if available for persistent session
if command -v tmux &> /dev/null; then
    echo "Launching in tmux session 'ib-tunnel'..."
    tmux new-session -d -s ib-tunnel "gh codespace ports forward 4002:localhost:4002 --codespace $CODESPACE_NAME" 2>/dev/null || \
    tmux new-session -s ib-tunnel "gh codespace ports forward 4002:localhost:4002 --codespace $CODESPACE_NAME"
    echo "Tunnel running in background. To view: tmux attach -t ib-tunnel"
else
    gh codespace ports forward 4002:localhost:4002 --codespace "$CODESPACE_NAME"
fi
