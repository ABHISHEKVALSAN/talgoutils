'''
This module performs unittest for calculator 
'''
import unittest
import talgoutils.constants as const
import talgoutils.calculator as calc

class Testing(unittest.TestCase):
    '''
    This class performs unittests on all the functions in talgoutils.calculator
    '''
    def test_get_pl(self):
        '''
        Unittest function to validate the function get_pl()
        '''
        kite_result = calc.get_pl(0, 0, 0, const.INTRADAY_EQ, const.KITE,
                                                                    const.NSE)
        binance_result = calc.get_pl(0, 0, 0, const.INTRADAY_EQ, const.BINANCE,
                                                                const.BINANCE)
        upstox_result = calc.get_pl(0, 0, 0, const.INTRADAY_EQ, const.UPSTOX,
                                                                    const.NSE)

        self.assertIsNotNone(kite_result)
        self.assertIsNotNone(binance_result)
        self.assertIsNotNone(upstox_result)


    def test_kite_pl(self):
        '''
        Unittest function to validate the method get_kite_pl()
        '''
        net_pl = calc.get_kite_pl(1000,1100,400,const.INTRADAY_EQ)
        self.assertTrue(round(net_pl * 100)/100.0==39795.76)

        net_pl = calc.get_kite_pl(1000,1100,40,const.INTRADAY_EQ)
        self.assertTrue(round(net_pl * 100)/100.0==3954.56)

        net_pl = calc.get_kite_pl(100,110,4,const.INTRADAY_EQ)
        self.assertTrue(round(net_pl * 100)/100.0==39.66)

        net_pl = calc.get_kite_pl(110,100,4,const.INTRADAY_EQ)
        self.assertTrue(round(net_pl * 100)/100.0==-40.34)

        net_pl = calc.get_kite_pl(1000,1100,400,const.DELIVERY_EQ)
        self.assertTrue(round(net_pl * 100)/100.0==39064.96)

        net_pl = calc.get_kite_pl(1000,1100,40,const.DELIVERY_EQ)
        self.assertTrue(round(net_pl * 100)/100.0==3906.5)

        net_pl = calc.get_kite_pl(100,110,4,const.DELIVERY_EQ)
        self.assertTrue(round(net_pl * 100)/100.0==38.9)

        net_pl = calc.get_kite_pl(110,100,4,const.DELIVERY_EQ)
        self.assertTrue(round(net_pl * 100)/100.0==-41.11)

        net_pl = calc.get_kite_pl(1000,1100,400,const.FNO_FUTURES, const.NSE)
        self.assertTrue(round(net_pl * 100)/100.0==39880.14)

        net_pl = calc.get_kite_pl(1000,1100,400,const.FNO_FUTURES, const.BSE)
        self.assertTrue(round(net_pl * 100)/100.0==39899.96)

        net_pl = calc.get_kite_pl(1000,1100,40,const.FNO_FUTURES, const.NSE)
        self.assertTrue(round(net_pl * 100)/100.0==3963.4)

        net_pl = calc.get_kite_pl(1000,1100,40,const.FNO_FUTURES, const.BSE)
        self.assertTrue(round(net_pl * 100)/100.0==3965.38)

        net_pl = calc.get_kite_pl(100,110,4,const.FNO_FUTURES, const.NSE)
        self.assertTrue(round(net_pl * 100)/100.0==39.67)

        net_pl = calc.get_kite_pl(100,110,4,const.FNO_FUTURES, const.BSE)
        self.assertTrue(round(net_pl * 100)/100.0==39.7)

        net_pl = calc.get_kite_pl(110,100,4,const.FNO_FUTURES, const.NSE)
        self.assertTrue(round(net_pl * 100)/100.0==-40.33)

        net_pl = calc.get_kite_pl(110,100,4,const.FNO_FUTURES, const.BSE)
        self.assertTrue(round(net_pl * 100)/100.0==-40.3)

        net_pl = calc.get_kite_pl(1000,1100,400, const.FNO_OPTIONS, const.NSE)
        self.assertTrue(round(net_pl * 100)/100.0==39194.62)

        net_pl = calc.get_kite_pl(1000,1100,400, const.FNO_OPTIONS, const.BSE)
        self.assertTrue(round(net_pl * 100)/100.0==39719.96)

        net_pl = calc.get_kite_pl(1000,1100,40, const.FNO_OPTIONS, const.NSE)
        self.assertTrue(round(net_pl * 100)/100.0==3876.99)

        net_pl = calc.get_kite_pl(1000,1100,40, const.FNO_OPTIONS, const.BSE)
        self.assertTrue(round(net_pl * 100)/100.0==3929.52)

        net_pl = calc.get_kite_pl(100,110,4, const.FNO_OPTIONS, const.NSE)
        self.assertTrue(round(net_pl * 100)/100.0==-7.74)

        net_pl = calc.get_kite_pl(100,110,4, const.FNO_OPTIONS, const.BSE)
        self.assertTrue(round(net_pl * 100)/100.0==-7.21)

        net_pl = calc.get_kite_pl(110,100,4, const.FNO_OPTIONS, const.NSE)
        self.assertTrue(round(net_pl * 100)/100.0==-87.74)

        net_pl = calc.get_kite_pl(110,100,4, const.FNO_OPTIONS, const.BSE)
        self.assertTrue(round(net_pl * 100)/100.0==-87.21)

        with self.assertRaises(SystemExit) as system_exit:
            calc.get_kite_pl(0,0,0,'gibberish')
        self.assertEqual(system_exit.exception.code, 1)

    def test_binance_pl(self):
        '''
        Unittest function to validate the method get_binance_pl()
        '''
        self.assertIsNotNone(self)

    def test_upstox_pl(self):
        '''
        Unittest fucntion to validate the method get_upstox_pl()
        '''
        self.assertIsNotNone(self)

if __name__=='__main__':
    unittest.main()
