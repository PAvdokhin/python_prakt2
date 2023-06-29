class Sneakers:

    def __init__(self, brand, cost):
        self.brand = brand
        self.cost = cost

    def __purchase_confirmed(self):
        print('Покупка успешна!')

    def sneakers_buy(self):
        self.__purchase_confirmed()
        print('Вы приобрели кроссовки', self.brand, 'по цене', self.cost, 'рублей)')


sneakers1 = Sneakers('adidas', 12990)
sneakers1.sneakers_buy()
sneakers2 = Sneakers('nike', 10990)
sneakers2.sneakers_buy()