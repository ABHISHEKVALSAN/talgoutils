import talgoutils.constants as const
import talgoutils.calculator as calc
import unittest


class Testing(unittest.TestCase):
    def test_get_pl(self):

        kite_result = calc.get_pl(0,0,0,const.INTRADAY_EQ,const.KITE)
        binance_result = calc.get_pl(0,0,0,const.INTRADAY_EQ,const.BINANCE)
        upstox_result = calc.get_pl(0,0,0,const.INTRADAY_EQ,const.UPSTOX)

        self.assertIsNotNone(kite_result)
        self.assertIsNotNone(binance_result)
        self.assertIsNotNone(upstox_result)


    def test_kite_pl(self):

        net_pl = calc.get_kite_pl(1000,1100,400,const.INTRADAY_EQ)
        net_pl = round(net_pl * 100)/100.0
        self.assertTrue(net_pl==39795.76)

        net_pl = calc.get_kite_pl(1000,1100,40,const.INTRADAY_EQ)
        net_pl = round(net_pl * 100)/100.0
        self.assertTrue(net_pl==3954.56)

        net_pl = calc.get_kite_pl(100,110,4,const.INTRADAY_EQ)
        net_pl = round(net_pl * 100)/100.0
        self.assertTrue(net_pl==39.66)

        net_pl = calc.get_kite_pl(110,100,4,const.INTRADAY_EQ)
        net_pl = round(net_pl * 100)/100.0
        self.assertTrue(net_pl==-40.34)

        net_pl = calc.get_kite_pl(1000,1100,400,const.DELIVERY_EQ)
        net_pl = round(net_pl * 100)/100.0
        self.assertTrue(net_pl==39064.96)

        net_pl = calc.get_kite_pl(1000,1100,40,const.DELIVERY_EQ)
        net_pl = round(net_pl * 100)/100.0
        self.assertTrue(net_pl==3906.5)

        net_pl = calc.get_kite_pl(100,110,4,const.DELIVERY_EQ)
        net_pl = round(net_pl * 100)/100.0
        self.assertTrue(net_pl==38.9)

        net_pl = calc.get_kite_pl(110,100,4,const.DELIVERY_EQ)
        net_pl = round(net_pl * 100)/100.0
        self.assertTrue(net_pl==-41.11)

        net_pl = calc.get_kite_pl(1000,1100,400,const.FNO_FUTURES, const.NSE)
        net_pl = round(net_pl * 100)/100.0
        self.assertTrue(net_pl==39880.14)

        net_pl = calc.get_kite_pl(1000,1100,400,const.FNO_FUTURES, const.BSE)
        net_pl = round(net_pl * 100)/100.0
        self.assertTrue(net_pl==39899.96)

        net_pl = calc.get_kite_pl(1000,1100,40,const.FNO_FUTURES, const.NSE)
        net_pl = round(net_pl * 100)/100.0
        self.assertTrue(net_pl==3963.4)

        net_pl = calc.get_kite_pl(1000,1100,40,const.FNO_FUTURES, const.BSE)
        net_pl = round(net_pl * 100)/100.0
        self.assertTrue(net_pl==3965.38)

        net_pl = calc.get_kite_pl(100,110,4,const.FNO_FUTURES, const.NSE)
        net_pl = round(net_pl * 100)/100.0
        self.assertTrue(net_pl==39.67)

        net_pl = calc.get_kite_pl(100,110,4,const.FNO_FUTURES, const.BSE)
        net_pl = round(net_pl * 100)/100.0
        self.assertTrue(net_pl==39.7)

        net_pl = calc.get_kite_pl(110,100,4,const.FNO_FUTURES, const.NSE)
        net_pl = round(net_pl * 100)/100.0
        self.assertTrue(net_pl==-40.33)

        net_pl = calc.get_kite_pl(110,100,4,const.FNO_FUTURES, const.BSE)
        net_pl = round(net_pl * 100)/100.0
        self.assertTrue(net_pl==-40.3)

        net_pl = calc.get_kite_pl(1000,1100,400, const.FNO_OPTIONS, const.NSE)
        net_pl = round(net_pl * 100)/100.0
        self.assertTrue(net_pl==39194.62)

        net_pl = calc.get_kite_pl(1000,1100,400, const.FNO_OPTIONS, const.BSE)
        net_pl = round(net_pl * 100)/100.0
        self.assertTrue(net_pl==39719.96)

        net_pl = calc.get_kite_pl(1000,1100,40, const.FNO_OPTIONS, const.NSE)
        net_pl = round(net_pl * 100)/100.0
        self.assertTrue(net_pl==3876.99)

        net_pl = calc.get_kite_pl(1000,1100,40, const.FNO_OPTIONS, const.BSE)
        net_pl = round(net_pl * 100)/100.0
        self.assertTrue(net_pl==3929.52)

        net_pl = calc.get_kite_pl(100,110,4, const.FNO_OPTIONS, const.NSE)
        net_pl = round(net_pl * 100)/100.0
        self.assertTrue(net_pl==-7.74)

        net_pl = calc.get_kite_pl(100,110,4, const.FNO_OPTIONS, const.BSE)
        net_pl = round(net_pl * 100)/100.0
        self.assertTrue(net_pl==-7.21)

        net_pl = calc.get_kite_pl(110,100,4, const.FNO_OPTIONS, const.NSE)
        net_pl = round(net_pl * 100)/100.0
        self.assertTrue(net_pl==-87.74)

        net_pl = calc.get_kite_pl(110,100,4, const.FNO_OPTIONS, const.BSE)
        net_pl = round(net_pl * 100)/100.0
        self.assertTrue(net_pl==-87.21)

        with self.assertRaises(SystemExit) as cm:
            calc.get_kite_pl(0,0,0,'gibberish')
        self.assertEqual(cm.exception.code, 1)

    def test_binance_pl(self):

        self.assertTrue(True)

    def test_upstox_pl(self):

        self.assertTrue(True)

if __name__=='__main__':
    unittest.main()
