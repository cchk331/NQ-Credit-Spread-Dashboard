# NQ Credit Spread Signal Dashboard

Live NQ futures credit spread signaling dashboard using Interactive Brokers API with RSI/Stochastic/MACD multi-timeframe analysis.

## Features

- **Multi-Timeframe Analysis**: RSI-14, Stochastic K/D-14, MACD 12/26/9 on 1h, 30m, and 1m charts
- **Credit Spread Signals**: Generates PUT or CALL credit spread signals (30-delta short / 20-delta long)
- **Live Portfolio Dashboard**: Net liquidation, cash, buying power, margin, PnL, open positions
- **Auto-Refresh**: Updates every 30 seconds with live IB data
- **User-Friendly HTML Dashboard**: Visual indicator bars, signal badges, portfolio cards

## Quick Start with GitHub Codespaces

1. Click **Code** > **Codespaces** > **Create codespace on main**
2. Wait for the environment to build (installs Python, Jupyter, ib_insync automatically)
3. Open `NQ_Credit_Spread_Dashboard.ipynb` in the Jupyter extension
4. Run cells 1-4 sequentially, then cell 5 for auto-refresh

## IB Gateway Setup

The notebook connects to IB Gateway/TWS via environment variables:

```
IB_HOST=127.0.0.1  (default)
IB_PORT=4002       (default, IB Gateway paper trading)
IB_CLIENT=0        (default, master client)
```

To connect from Codespaces, you need IB Gateway running on a reachable host. Options:
- Run IB Gateway locally and use port forwarding
- Run IB Gateway in a Docker container within Codespaces
- Set `IB_HOST` to your IB Gateway server IP

## Strategy

| Signal | Condition | Trade |
|--------|-----------|-------|
| BULLISH | RSI>50 + MACD>Signal + StochK>D on all TFs | Sell PUT credit spread |
| BEARISH | RSI<50 + MACD<Signal + StochK<D on all TFs | Sell CALL credit spread |
| NEUTRAL | Indicators not aligned | No trade |

## Files

- `NQ_Credit_Spread_Dashboard.ipynb` - Main dashboard notebook
- `.devcontainer/devcontainer.json` - Codespaces configuration
- `requirements.txt` - Python dependencies
