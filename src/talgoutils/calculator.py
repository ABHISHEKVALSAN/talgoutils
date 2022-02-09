'''
Set of function to determine the brokerage and tax deduction in various
platforms and exchanges
'''

import sys
import talgoutils.constants as const


def get_pl(buy, sell, qty, asset_class, platform, exchange):
    '''
    Get P&L from different platform upon a transaction
    '''

    if platform==const.KITE:
        return get_kite_pl(buy, sell, qty, asset_class, exchange)
    if platform==const.BINANCE:
        return get_binance_pl(buy, sell, qty, asset_class)
    if platform==const.UPSTOX:
        return get_upstox_pl(buy, sell,  qty, asset_class)
    print('')

def get_kite_pl(buy, sell, qty, asset_class, exchange=const.NSE):
    '''
    Get P&L according to zerodha calculator
    '''

    turnover = (buy + sell) * qty

    if asset_class == const.INTRADAY_EQ:

        brokerage = min(round(turnover * 0.03) * 0.01, 40)
        stt_total = int(round(sell * qty * 0.025) * 0.01)
        ex_trans_chrg =  round(turnover * 0.00345) * 0.01
        gst = (brokerage + ex_trans_chrg) * 0.18
        sebi_chrg = round(turnover * 0.0001) * 0.01
        stamp_chrg = round(buy * qty * 0.003) * 0.01

        total_tax = brokerage + stt_total + ex_trans_chrg + gst + sebi_chrg +\
                                                                    stamp_chrg

        net_pl = (sell - buy) * qty - total_tax

        return net_pl

    if asset_class == const.DELIVERY_EQ:

        brokerage = 0 #always
        stt_total = round(round(turnover * 0.1) * 0.01)
        ex_trans_chrg =  round(turnover * 0.00345) * 0.01
        gst = (brokerage + ex_trans_chrg) * 0.18
        sebi_chrg = round(turnover * 0.01 *0.01) * 0.01
        stamp_chrg = round(buy * qty * 0.015) * 0.01

        total_tax = brokerage + stt_total + ex_trans_chrg + gst + sebi_chrg +\
                                                                    stamp_chrg

        net_pl = (sell - buy) * qty - total_tax

        return net_pl
    if asset_class == const.FNO_FUTURES:

        brokerage = min(round(turnover * 0.03) * 0.01, 40)
        stt_total = round(sell * qty * 0.01 * 0.01)
        if exchange == const.NSE:
            ex_trans_chrg =  round(turnover * 0.002) * 0.01
        else:
            ex_trans_chrg = 0
        gst = (brokerage + ex_trans_chrg) * 0.18
        sebi_chrg = round(turnover * 0.0001) * 0.01
        stamp_chrg = round(buy * qty * 0.002) * 0.01

        total_tax = brokerage + stt_total + ex_trans_chrg + gst + sebi_chrg +\
                                                                    stamp_chrg

        net_pl = (sell - buy) * qty - total_tax

        return net_pl
    if asset_class == const.FNO_OPTIONS:

        brokerage = 40
        stt_total = round(sell * qty * 0.05 * 0.01)
        if exchange == const.NSE:
            ex_trans_chrg = round(turnover * 0.053) * 0.01
        else:
            ex_trans_chrg = 0
        gst = (brokerage + ex_trans_chrg) * 0.18
        sebi_chrg = round(turnover * 0.01 * 0.01) * 0.01
        stamp_chrg = round(buy * qty * 0.003) * 0.01

        total_tax = brokerage + stt_total + ex_trans_chrg + gst + sebi_chrg +\
                                                                    stamp_chrg

        net_pl = (sell - buy) * qty - total_tax

        # print('brokerage : ',brokerage)
        # print('stt_total : ', stt_total)
        # print('ex_trans_chrg : ', ex_trans_chrg)
        # print('gst : ', gst)
        # print('sebi_chrg : ', sebi_chrg)
        # print('stamp_chrg', stamp_chrg)
        # print(net_pl)

        return net_pl
    print('Unknown asset class.')
    sys.exit(1)

def get_binance_pl(buy, sell, qty, asset_class):
    '''
    Get P&L after a binance transaction
    '''
    total_tax = 0
    if asset_class:
        net_pl = (sell - buy) * qty - total_tax
    if not asset_class:
        net_pl = (sell - buy) * qty - total_tax
    return net_pl

def get_upstox_pl(buy, sell, qty, asset_class):
    '''
    Get P&L after transaction in upstox
    '''
    total_tax = 0
    if asset_class:
        net_pl = (sell - buy) * qty - total_tax
    if not asset_class:
        net_pl = (sell - buy) * qty - total_tax
    return net_pl
