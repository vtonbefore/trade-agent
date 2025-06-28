import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model
def load_model():
    return joblib.load("model.pkl")

model = load_model()

st.set_page_config(page_title="TradeHub AI", layout="centered")
st.title("📈 Welcome to TradeHub AI")
st.markdown("""
This AI assistant predicts market movement based on technical indicators.
Enter your values to see a prediction and trade decision.
""")

st.subheader("🔢 Input Your Technical Indicators")

with st.form("prediction_form"):
    rsi = st.number_input("RSI", min_value=0.0, max_value=100.0, value=50.0)
    macd = st.number_input("MACD", value=0.0)
    macd_signal = st.number_input("MACD Signal", value=0.0)
    ema_12 = st.number_input("EMA 12", value=0.0)
    ema_26 = st.number_input("EMA 26", value=0.0)
    bb_upper = st.number_input("Bollinger Upper", value=0.0)
    bb_lower = st.number_input("Bollinger Lower", value=0.0)
    volume = st.number_input("Volume", value=100000.0)
    submitted = st.form_submit_button("🔍 Predict")

if submitted:
    features = np.array([[rsi, macd, macd_signal, ema_12, ema_26, bb_upper, bb_lower, volume]])
    prediction = model.predict(features)[0]
    confidence = model.predict_proba(features).max()

    label = "UP" if prediction == 1 else "DOWN"
    decision = "Buy" if prediction == 1 else "Sell"

    st.success(f"📊 Prediction: {label}")
    st.metric("Confidence", f"{confidence * 100:.2f}%")
    st.metric("Suggested Action", decision)

    if confidence < 0.7:
        st.warning("⚠️ Confidence is low. Consider confirming with other analysis tools.")
