def is_green_candle(df):
    if df.open[0]<df.close[0]:
        return True
    return False

def is_red_candle(df):
    if df.open[0]>df.close[0]:
        return True
    return False

def is_doge_candle(df):
    if ~is_green_candle(df) and ~is_red_candle(df):
        return True
    return False
