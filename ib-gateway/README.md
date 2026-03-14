# IB Gateway Local Setup

This Docker setup runs IB Gateway on your **local machine** and tunnels the connection to GitHub Codespaces.

## Quick Start

### 1. Setup credentials
```bash
cd ib-gateway
cp .env.example .env
# Edit .env with your IB credentials
```

### 2. Start IB Gateway
```bash
docker-compose up -d
docker-compose logs -f
```

### 3. Approve 2FA on IBKR Mobile app (first time)
Watch logs for: `Waiting for 2FA approval...`
Then approve on your phone.

### 4. Tunnel to your Codespace
```bash
# List your codespaces
gh codespace list

# Forward port (keep this terminal open or use tmux)
gh codespace ports forward 4002:localhost:4002 --codespace <your-codespace-name>
```

### 5. Test connection inside Codespace
```bash
python scripts/healthcheck.py
```

## Ports
| Port | Purpose |
|------|---------|
| 4002 | Paper trading API |
| 4001 | Live trading API |
| 5900 | VNC monitoring |

## Keep tunnel alive (optional)
```bash
tmux new -s ib-tunnel
gh codespace ports forward 4002:localhost:4002 --codespace <name>
# Detach: Ctrl+B then D
# Reattach: tmux attach -t ib-tunnel
```
