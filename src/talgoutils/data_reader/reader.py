import pandas as pd

def read_csv(path):
    df = pd.read_csv(path)
    return df

def read_parquet(path):
    df = pd.read_parquet(path)
    return df

def read_orc(path):
    df = pd.read_orc(path)
    return df

def read_gz(path):

    return df

def read_zip(path):
    return df
