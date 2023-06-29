class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise ValueError("Имя должно быть string")

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if isinstance(age, int) and age >= 0:
            self.__age = age
        else:
            raise ValueError("Возраст не может быть отрицательным")


pers1 = Person("Алина", 21)
pers1.set_name("Алина")
pers1.set_age(21)