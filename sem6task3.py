import time

a = input('Введите дату своего рождения (dd/mm/yyyy) - ')
print(f"Вы существуете столько дней: ", int(time.time()-time.mktime(time.strptime(a, '%d/%m/%Y'))) // 86400)

