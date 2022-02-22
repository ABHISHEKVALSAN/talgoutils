from datetime import datetime as dt, timedelta as td
from talgoutils import constants as const
from talgoutils.data_reader import reader
import talgoutils.env as env
import glob
import numpy as np
import random
import pandas as pd
import os

def get_data(asset_detail):
    df = pd.DataFrame()
    for csv_file in glob.glob(os.path.join(asset_detail['path'],'*.csv')):
        df = reader.read_data(csv_file)
    return df

def feed_sequential_data(
    exchange='NSE', asset_class='EQ', asset_list=const.NIFTY50,
    interval='5minute', start_date=None, end_date=None):


    iter_date=end_date
    while iter_date>=start_date:
        for asset in asset_list:
            asset_detail['exchange'] = exchange
            asset_detail['class'] = asset_class
            asset_detail['interval'] = interval
            asset_detail['date'] = iter_date
            asset_detail['symbol'] = asset
            asset_detail['path']  =  os.path.join( env.DATA_PATH, exchange,
                                        asset_class, random_asset, interval,
                                        random_date.strftime('y=%Y/m=%m/d=%d'))
            asset_detail['data'] = get_asset(asset_detail)
            yield asset_detail
        iter_date =  iter_date - timedelta(days=1)


def feed_random_data(
    exchange='NSE', asset_class='EQ', asset_list=const.NIFTY50,
    interval='5minute', start_date=dt(2015,2,2), end_date=dt(2021,10,31)):

    while True:

        random_asset = random.choice(asset_list)
        random_date = start_date + td(days=random.randrange(
                                        (end_date - start_date).days))
        random_path = os.path.join(
                                env.DATA_PATH,
                                exchange,
                                asset_class,
                                random_asset,
                                interval,
                                random_date.strftime('y=%Y/m=%m/d=%d'))
        if os.path.exists(random_path) is not True:
            continue
        asset_detail = {}
        asset_detail['exchange'] = exchange
        asset_detail['class'] = asset_class
        asset_detail['interval'] = interval
        asset_detail['date'] = random_date
        asset_detail['symbol'] = random_asset
        asset_detail['path'] = random_path
        asset_detail['data'] = get_data(asset_detail)
        yield asset_detail
