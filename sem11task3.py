class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    def emp_info(self):
        return "Name: {}, Position: {}, Salary: {}".format(self.name, self.position, self.salary)


class Waiter(Employee):
    def __init__(self, name, salary):
        super().__init__(name, 'Waiter', salary)
    def emp_info(self):
        return "Name: {}, Position: {}, Salary: {}".format(self.name, self.position, self.salary)

class Oguzok(Employee):
    def __init__(self, name, salary, duty):
        super().__init__(name, "Oguzok", salary)
        self.duty = duty
    def emp_info(self):
        return "Name: {}, Position: {}, Salary: {}, Duty: {} ".format(self.name, self.position, self.salary, self.duty)

class Chef(Employee):
    def __init__(self, name, salary, experience):
        super().__init__(name, "Chef", salary)
        self.experience = experience
    def emp_info(self):
        return "Name: {}, Position: {}, Salary: {}, Experience(%): {}".format(self.name, self.position, self.salary, self.experience)

waiter1 = Waiter("Саша", 15000)
oguzok = Oguzok('Макс', 35000, "Убирать этикетки с бананов")
chef = Chef('Виктор Петрович', 1000000, "Лучший повар кухни")

print(waiter1.emp_info())
print(oguzok.emp_info())
print(chef.emp_info())