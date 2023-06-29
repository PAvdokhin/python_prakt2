class BankAccount:
    def __init__(self, name, number, balance, password):
        self.name = name
        self.number = number
        self.__balance = balance
        self.__password = password

    def get_balance(self, password):
        if password == self.__password:
            return self.__balance
        else:
            return "Неверный пароль"

    def set_balance(self, new_balance, password):
        if password == self.__password:
            self.__balance = new_balance
            return "Баланс обновился"
        else:
            return "Ошибка!"


owner = BankAccount("Олег", 128, 2300, 0000)
print(owner.get_balance(1111))
print((owner.get_balance(0000)))
print(owner.set_balance(100, 0000))
print(owner .get_balance(0000))
