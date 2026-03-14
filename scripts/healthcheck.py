#!/usr/bin/env python3
"""
IB Gateway Health Check
Run this inside Codespaces to verify tunnel connection is working.
Usage: python scripts/healthcheck.py
"""

import sys
import time
from ib_insync import IB

IB_HOST = '127.0.0.1'
IB_PORT = 4002        # Paper trading port
CLIENT_ID = 999      # Use high ID to avoid conflicts
TIMEOUT = 10

def check_connection():
    ib = IB()
    try:
        print(f"Connecting to IB Gateway at {IB_HOST}:{IB_PORT}...")
        ib.connect(IB_HOST, IB_PORT, clientId=CLIENT_ID, timeout=TIMEOUT)

        account = ib.managedAccounts()[0]
        print(f"✓ Connected successfully")
        print(f"✓ Account: {account}")
        print(f"✓ Server time: {ib.reqCurrentTime()}")

        # Check market data subscription
        summary = ib.accountSummary(account)
        net_liq = next((s.value for s in summary if s.tag == 'NetLiquidation'), 'N/A')
        print(f"✓ Net Liquidation: ${float(net_liq):,.2f}" if net_liq != 'N/A' else "✓ Account summary retrieved")

        print("\n✅ IB Gateway tunnel is working correctly!")
        return True

    except Exception as e:
        print(f"\n✗ Connection failed: {e}")
        print("\nTroubleshooting:")
        print("  1. Is IB Gateway Docker running locally? → docker-compose ps")
        print("  2. Is the tunnel active? → gh codespace ports forward 4002:localhost:4002")
        print("  3. Did you approve 2FA on IBKR Mobile?")
        return False

    finally:
        if ib.isConnected():
            ib.disconnect()

if __name__ == '__main__':
    ok = check_connection()
    sys.exit(0 if ok else 1)
