class Monkey:
    def __init__(self, name, size, brains, voice, looks, personal_rating):
        self.name = name
        self.size = size #примерный размер в см
        #все следующие хар-ки оцениваются от 0 до 10 по собвенному мнению
        self.brains = brains
        self.voice = voice
        self.personal_rating = personal_rating
        self.looks = looks


chimpanzee = Monkey("Шимпанзе", '120 - 150 см', 10, 8, 5, 7.5)
gibbon = Monkey('Гиббон', '45 - 90 см', 7, 5, 5, 10) #10 - потому что у них название прикольное
howler = Monkey('Ревун', '40 - 70 см', 5, 10, 8, 7.5)
gorilla = Monkey('Горилла', '150 - 200 см', 8.5, 8, 10, 9)


print('ИДЕАЛЬНАЯ ОБЕЗЬЯНА')
print(gorilla.looks)
print(chimpanzee.brains)
print(howler.voice)
print(gibbon.personal_rating)




