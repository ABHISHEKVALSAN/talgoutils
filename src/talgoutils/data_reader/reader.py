import pandas as pd
from talgoutils import constants as const

def read_data(filename):
    '''
    Understand the file format and the file location from the filename, and
    read data according. Filepath can also be URI in the future.

    Example: wasb://<my_container>/path/to/file.csv or s3://<bucket>/path/to/
    file.csv

    params: filename str
    rparam: df pandas.DataFrame
    '''

    if filename.endswith(const.CSV):
        return read_csv(filename)
    elif filename.endsiwth(const.PARQUET):
        return read_parquet(filename)
    elif filename.endswith(const.ORC):
        return read_orc(filename)
    else:
        print('Warning: Unknown file format for file {}'.format(filename))

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
