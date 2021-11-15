from datetime import datetime as dt, timedelta as td


def get_daily(time, format='y=%Y/m=%m/d=%d'):
    return (dt.now()-td(days=1)).strftime(format)

def get_hourly(time, format='y=%Y/m=%m/d=%d/h=%h'):
    return (dt.now()-td(hour=1)).strftime(format)

def get_weekly(time, format='y=%Y/w=%W'):
    return (dt.now()-td(days=7)).strftime(format)

def get_yearly(time, format='y=%Y'):
    return (dt.now()-td(year=1)).strftime(format)
