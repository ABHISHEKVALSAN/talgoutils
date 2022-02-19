import pandas as pd
import numpy as np
from datetime import datetime as dt, timedelta as td


def get_asset( asset_name, date):
    return asset_data

def feed_sequential_data(
                    asset_list=const.NIFTY50,
                    interval='5minute',
                    start_date,
                    end_date):
    for asset in asset_list:
        while iter_date>=start_date:
            iter_date = end_date
            asset_detail['date'] = iter_date
            asset_detail['symbol'] = random_asset
            asset_detail['data'] = get_asset(asset_name, asset_date)
            yield asset_detail
            iter_date =  iter_date - timedelta(days=1)


def feed_random_data(
    exchange='NSE', asset_class='EQ', asset_list=const.NIFTY50,
    interval='5minute', start_date=None, end_date=None):


    while True:

        random_asset = random.choice(asset_list)
        random_date = start_date + td(days = random.randrange((end_date - start_date).days))
        random_path = os.path.join(
                                const.DATA_PATH,
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
        asset_detail['path'] = random_path
        asset_detail['symbol'] = random_asset
        asset_detail['data'] = get_stock(asset_detail)
        yield asset_detail
