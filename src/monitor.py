
import time
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(
    filename="logs\monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def log_trade(action, price, balance):
    msg = f"Trade executed: {action} at ${price:.2f} | Balance: ${balance:.2f}"
    logging.info(msg)
    print("[MONITOR]", msg)


def alert_signal(label, confidence):
    if confidence >= 0.85:
        msg = f"⚠️ High confidence signal: {label} ({confidence * 100:.1f}%)"
        logging.warning(msg)
        print("[ALERT]", msg)


def monitor_loop():
    while True:
        now = datetime.now().strftime("%H:%M:%S")
        logging.info(f"Heartbeat check at {now}")
        print(f"[HEARTBEAT] {now}")
        time.sleep(60)


if __name__ == "__main__":
    monitor_loop()
