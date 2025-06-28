
import time

def execute_trade(action, dry_run=True):
    """
    Executes a trade action.
    - action: "BUY", "SELL", or "HOLD"
    - dry_run: if True, will not place real trades
    """
    if action == "HOLD":
        print("[=] No action taken (HOLD)")
        return

    if dry_run:
        print(f"[SIMULATION] Would execute: {action}")
    else:
        # Placeholder for real TradeHub or broker API integration
        print(f"[TRADE] Executing real trade: {action}")
        time.sleep(1)  # Simulate API delay
        print("[✓] Trade executed successfully")

if __name__ == "__main__":
    execute_trade("BUY")
