class KiteOrder(kite):
    def __init__(self, kite, order_id, kws=None):
        self.kite = kite
        self.order_id = order_id

    def place_mis_order(self):
        '''
        Place a market order
        '''
        pass

    def place_cover_order(self):
        '''
        Place a cover order with a stoploss
        '''
        pass

    def place_bracket_order(self):
        '''
        Place a bracket order (OCO order) with a target and stoploss
        '''
        pass

    def trail_order(self, trail_strategy):
        '''
        Trails the stoploss of a given order according to some strategy.
        Relevant for cover orders and bracket orders
        '''
        pass
