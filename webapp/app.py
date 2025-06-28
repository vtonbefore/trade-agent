from fastapi import FastAPI
from pydantic import BaseModel
from src.predicts import predict_next_move
from src.decisions_engine import make_trade_decision

app = FastAPI()

class MarketData(BaseModel):
    rsi: float
    macd: float
    macd_signal: float
    ema_12: float
    ema_26: float
    bb_upper: float
    bb_lower: float
    volume: float

@app.get("/")
def root():
    return {"status": "TradeHub AI API is running"}

@app.post("/predict")
def predict_signal(data: MarketData):
    features = [[
        data.rsi, data.macd, data.macd_signal,
        data.ema_12, data.ema_26,
        data.bb_upper, data.bb_lower,
        data.volume
    ]]
    prediction, confidence = predict_next_move(features)
    decision = make_trade_decision(prediction, confidence)
    return {
        "prediction": prediction,
        "confidence": confidence,
        "decision": decision
    }
