class Warrior:
    def __init__(self, name, future):
        self.name = name
        self.future = future
    def info(self):
        print(f'{self.name} состоит в(о){self.future}')


class Thief:
    def __init__(self, name, future):
        self.name = name
        self.future = future

    def victory(self, warrior):
        print(f'{self.name} убеждает воина по имени {warrior.name} перейти в(о) {self.future} ')
    def changing_future(self, warrior):
        warrior.future = self.future


warrior_1 = Warrior('Олег', 'фракция воинов')
thief_1 = Thief('Тарзан', 'фракция воров')
warrior_1.info()
thief_1.victory(warrior_1)
thief_1.changing_future(warrior_1)
warrior_1.info()

