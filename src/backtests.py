import pandas as pd
import joblib
from src.features import compute_indicators
from src.decisions_engine import make_trade_decision

def run_backtest(csv_path="data/BTC_USDT_1h.csv", initial_balance=1000):
    # Load and compute indicators
    df = pd.read_csv(csv_path)
    df = compute_indicators(df)

    # Load trained model once
    model = joblib.load("models/xgb_model.pkl")

    balance = initial_balance
    position = None
    entry_price = 0

    for i in range(30, len(df)):
        row = df.iloc[i]

        X = df.iloc[[i]][[
            'rsi', 'macd', 'macd_signal', 'ema_12', 'ema_26',
            'bb_upper', 'bb_lower', 'volume'
        ]]

        prediction = model.predict(X)[0]
        proba = model.predict_proba(X)[0][prediction]
        label = "UP" if prediction == 1 else "DOWN"

        decision = make_trade_decision(label, proba)

        price = row["close"]

        if decision == "BUY" and position is None:
            position = "LONG"
            entry_price = price
            print(f"[+] Buy at {price:.2f}")

        elif decision == "SELL" and position == "LONG":
            pnl = price - entry_price
            balance += pnl
            print(f"[-] Sell at {price:.2f} | PnL: {pnl:.2f} | Balance: {balance:.2f}")
            position = None

    if position == "LONG":
        final_price = df.iloc[-1]["close"]
        pnl = final_price - entry_price
        balance += pnl
        print(f"[x] Final close at {final_price:.2f} | PnL: {pnl:.2f} | Balance: {balance:.2f}")

    print(f"[✓] Final balance: {balance:.2f}")

if __name__ == "__main__":
    run_backtest()
