# src/predict.py

import pandas as pd
import joblib
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.features import compute_indicators

def load_latest_data(csv_path="data/BTC_USDT_1h.csv"):
    df = pd.read_csv(csv_path)
    df = compute_indicators(df)
    return df.tail(1)  # get the latest row

def predict_next_move():
    model = joblib.load("models/xgb_model.pkl")
    df = load_latest_data()

    features = [
        'rsi', 'macd', 'macd_signal', 'ema_12', 'ema_26',
        'bb_upper', 'bb_lower', 'volume'
    ]
    X = df[features]
    prediction = model.predict(X)[0]
    proba = model.predict_proba(X)[0][prediction]

    label = "UP" if prediction == 1 else "DOWN"
    print(f"[+] Prediction: {label} ({round(proba * 100, 2)}% confidence)")
    return label, proba

if __name__ == "__main__":
    predict_next_move()
