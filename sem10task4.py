class Train:
    def __init__(self,destination, ticket_price, seats):
        self.destination = destination
        self.ticket_price = ticket_price
        self.seats = seats



class Passenger:
    def __init__(self, name, balance, destination):
        self.name = name
        self.balance = balance
        self.destination = destination
    def situation(self):
        print(f'{self.name} должен добраться до {self.destination}. Баланс: {self.balance} ')
    def buy(self, train):
        if self.destination == train.destination and self.balance >= train.ticket_price:
            self.balance = self.balance - train.ticket_price
            print(f'{self.name} получил сдачу в размере {self.balance} рублей и поехал в {self.destination}')
        else:
            print(f'{self.name} теперь живет на вокзале')


passenger1 = Passenger('Олег', 2400, 'Новокузнецк')
passenger2 = Passenger('Тарзан', 5, 'Новокузнецк')
train1 = Train('Новокузнецк', 1400, 25)

passenger1.situation()
passenger1.buy(train1)
passenger2.situation()
passenger2.buy(train1)






