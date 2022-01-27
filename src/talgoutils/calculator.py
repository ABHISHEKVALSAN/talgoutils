import talgoutils.constants as const
import sys

def get_pl(buy, sell, qty, asset_class, platform='kite'):

    if platform==const.KITE:
        return get_kite_pl(buy, sell, qty, asset_class)
    elif platform==const.BINANCE:
        return get_binance_pl(buy, sell, qty, asset_class)
    elif platform==const.UPSTOX:
        return get_upstox_pl(buy, sell,  qty, asset_class)

def get_kite_pl(buy, sell, qty, asset_class):

    total_amount = (buy + sell) * qty

    if asset_class == const.INTRADAY_EQ:
        brokerage = min(total_amount * 0.0003, 40)
        stt_total = sell * qty * 0.00025
        ex_trans_chrg =  total_amount * 0.00345 * 0.01
        gst = (brokerage + ex_trans_chrg) * 0.18
        sebi_chrg = total_amount * 0.001 * 0.001
        stamp_chrg = buy * qty * 0.03 * 0.001

        total_tax = brokerage + stt_total + ex_trans_chrg + gst + \
                    sebi_chrg + stamp_chrg

        net_pl = (sell - buy) * qty - total_tax

        # print('brokerage : ',brokerage)
        # print('stt_total : ', stt_total)
        # print('ex_trans_chrg : ', ex_trans_chrg)
        # print('gst : ', gst)
        # print('sebi_chrg : ', sebi_chrg)
        # print('stamp_chrg', stamp_chrg)

        return net_pl

    elif asset_class == const.DELIVERY_EQ:
        total_tax = 0
        net_pl = (sell - buy) * qty - total_tax
        return net_pl
    elif asset_class == const.FNO_FUTURES:
        total_tax = 0
        net_pl = (sell - buy) * qty - total_tax
        return net_pl
    elif asset_class == const.FNO_OPTIONS:
        total_tax = 0
        net_pl = (sell - buy) * qty - total_tax
        return net_pl
    else:
        print('Unknown asset class.')
        sys.exit(1)

def get_binance_pl(buy, sell, qty, asset_class):
    total_tax = 0
    net_pl = (sell - buy) * qty - total_tax
    return net_pl

def get_upstox_pl(buy, sell, qty, asset_class):
    total_tax = 0
    net_pl = (sell - buy) * qty - total_tax
    return net_pl
