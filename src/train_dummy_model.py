import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import joblib

# 1. Create dummy dataset with same features your dashboard uses
data = pd.DataFrame({
    "RSI": np.random.uniform(10, 90, 100),
    "MACD": np.random.normal(0, 1, 100),
    "MACD_Signal": np.random.normal(0, 1, 100),
    "EMA_12": np.random.uniform(100, 200, 100),
    "EMA_26": np.random.uniform(100, 200, 100),
    "BB_Upper": np.random.uniform(210, 230, 100),
    "BB_Lower": np.random.uniform(180, 200, 100),
    "Volume": np.random.uniform(10000, 1000000, 100),
    "Target": np.random.randint(0, 2, 100)  # 0 = DOWN, 1 = UP
})

# 2. Train/Test split
X = data.drop("Target", axis=1)
y = data["Target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train model
model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(X_train, y_train)

# 4. Save model as model.pkl
joblib.dump(model, "model.pkl")

print("✅ model.pkl saved successfully.")
