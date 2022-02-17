'''
Frequency module to generate path extension for daily weekly schedule runs,
in the structure that is intuitive and are required standards for data query
tools like presto while querying data lakes.
'''

from datetime import datetime as dt, timedelta as td

def get_daily(pathformat='y=%Y/m=%m/d=%d'):
    '''
    daily frequency provide path extension for daily runs
    '''
    return (dt.now()-td(days=1)).strftime(pathformat)

def get_bidaily(pathformat='y=%Y/m=%m/d=%d'):
    '''
    bidaily frequency provide path extension for runs that happens twice a day
    '''
    current_time=dt.now()
    if current_time.hour>=12:
        return (current_time-td(hour=1)).strftime(pathformat)+'/h=12'
    return (current_time-td(hour=1)).strftime(pathformat)+'/h=00'


def get_hourly(pathformat='y=%Y/m=%m/d=%d/h=%h'):
    '''
    hourly frequency provide path extension for runs that happens hourly
    '''
    return (dt.now()-td(hour=1)).strftime(pathformat)

def get_weekly(pathformat='y=%Y/w=%W'):
    '''
    For weekly runs
    '''
    return (dt.now()-td(days=7)).strftime(pathformat)

def get_biweekfly(pathformat='y=%Y/w=%W'):
    '''
    For biweekly runs
    '''
    current_time = dt.now()
    if current_time.weekday<=4:
        return (current_time-td(days=4)).strftime(pathformat)+'/d=00'
    return (current_time-td(days=4)).strftime(pathformat)+'/d=04'


def get_yearly(pathformat='y=%Y'):
    '''
    For yearly runs :/
    '''
    return (dt.now()-td(year=1)).strftime(pathformat)
