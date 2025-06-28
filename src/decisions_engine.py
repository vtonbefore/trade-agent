
def make_trade_decision(prediction_label, confidence, min_confidence=0.6):
    """
    Decide whether to BUY, SELL, or HOLD based on prediction and confidence.
    - prediction_label: "UP" or "DOWN"
    - confidence: 0.0 to 1.0
    - min_confidence: threshold to trigger a trade
    """
    if confidence < min_confidence:
        return "HOLD"

    if prediction_label == "UP":
        return "BUY"
    elif prediction_label == "DOWN":
        return "SELL"
    else:
        return "HOLD"

if __name__ == "__main__":
    print("[+] Decision Engine ready.")
