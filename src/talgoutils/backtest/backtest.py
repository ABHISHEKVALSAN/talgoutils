import pandas as pd
import numpy as np
from datetime import datetime as dt, timedelta as td


def get_stock( stock_name, date):
    return stock_data


def feed_sequential_data(
                    stock_list=const.NIFTY50,
                    interval='5minute',
                    start_date,
                    end_date):
    for stock in stock_list:
        while iter_date>=start_date:
            iter_date = end_date
            stock_detail['date'] = iter_date
            stock_detail['symbol'] = random_stock
            stock_detail['data'] = get_stock(stock_name, stock_date)
            yield stock_detail
            iter_date =  iter_date - timedelta(days=1)


def feed_random_data(
                        stock_list=const.NIFTY50,
                        interval='5minute',
                        start_date,
                        end_date
                ):
    random_date = get_random_date(start_date, end_date)
    randome_stock = random.choice(stock_list)

    stock['date'] = random_date
    stock['symbol'] = random_stock
    stock['data'] = get_stock(randome_stock, random_date, interval)


    yield stock_detail
