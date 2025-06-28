
import pandas as pd
import ta

def compute_indicators(df):
    """
    Compute technical indicators: RSI, MACD, EMA, Bollinger Bands
    """
    df = df.copy()
    
    # Ensure column types
    df['close'] = pd.to_numeric(df['close'], errors='coerce')
    df['high'] = pd.to_numeric(df['high'], errors='coerce')
    df['low'] = pd.to_numeric(df['low'], errors='coerce')
    df['volume'] = pd.to_numeric(df['volume'], errors='coerce')

    # RSI
    df['rsi'] = ta.momentum.RSIIndicator(close=df['close']).rsi()

    # MACD
    macd = ta.trend.MACD(close=df['close'])
    df['macd'] = macd.macd()
    df['macd_signal'] = macd.macd_signal()

    # EMA
    df['ema_12'] = ta.trend.EMAIndicator(close=df['close'], window=12).ema_indicator()
    df['ema_26'] = ta.trend.EMAIndicator(close=df['close'], window=26).ema_indicator()

    # Bollinger Bands
    boll = ta.volatility.BollingerBands(close=df['close'])
    df['bb_upper'] = boll.bollinger_hband()
    df['bb_lower'] = boll.bollinger_lband()

    df = df.dropna()
    return df

if __name__ == "__main__":
    df = pd.read_csv("data/BTC_USDT_1h.csv")
    enriched_df = compute_indicators(df)
    enriched_df.to_csv("data/BTC_USDT_1h_enriched.csv", index=False)
    print("[+] Indicators computed and saved.")
