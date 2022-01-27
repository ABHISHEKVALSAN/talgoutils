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

        net_pl = calc.get_kite_pl(0,0,0,const.DELIVERY_EQ)
        net_pl = round(net_pl * 100)/100.0
        self.assertIsNotNone(net_pl)

        net_pl = calc.get_kite_pl(0,0,0,const.FNO_OPTIONS)
        net_pl = round(net_pl * 100)/100.0
        self.assertIsNotNone(net_pl)

        net_pl = calc.get_kite_pl(0,0,0,const.FNO_FUTURES)
        net_pl = round(net_pl * 100)/100.0
        self.assertIsNotNone(net_pl)

        with self.assertRaises(SystemExit) as cm:
            calc.get_kite_pl(0,0,0,'gibberish')
        self.assertEqual(cm.exception.code, 1)

    def test_binance_pl(self):

        self.assertTrue(True)

    def test_upstox_pl(self):

        self.assertTrue(True)

if __name__=='__main__':
    unittest.main()
