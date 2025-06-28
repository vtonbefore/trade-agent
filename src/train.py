
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import os
import joblib

def prepare_dataset(filepath):
    df = pd.read_csv(filepath)
    df['target'] = (df['close'].shift(-1) > df['close']).astype(int)
    
    features = [
        'rsi', 'macd', 'macd_signal', 'ema_12', 'ema_26',
        'bb_upper', 'bb_lower', 'volume'
    ]
    X = df[features].dropna()
    y = df['target'].loc[X.index]
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model():
    X_train, X_test, y_train, y_test = prepare_dataset("data/BTC_USDT_1h_enriched.csv")
    model = xgb.XGBClassifier(n_estimators=100, max_depth=3, learning_rate=0.1)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    print("\n[+] Classification Report:\n")
    print(classification_report(y_test, preds))

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/xgb_model.pkl")
    print("[+] Model saved to models/xgb_model.pkl")

if __name__ == "__main__":
    train_model()
