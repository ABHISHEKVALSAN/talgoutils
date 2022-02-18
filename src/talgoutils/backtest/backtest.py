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
                        asset_list=const.NIFTY50,
                        interval='5minute',
                        start_date,
                        end_date
                ):
    random_date = get_random_date(start_date, end_date)
    randome_asset = random.choice(asset_list)

    asset_detail['date'] = random_date
    asset_detail['symbol'] = random_asset
    asset_detail['data'] = get_asset(randome_asset, random_date, interval)
    asset_detail['']


    yield asset_detail
