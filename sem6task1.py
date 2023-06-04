import time
a = int(input('Введите число - '))
while a > 0:
    time.sleep(a)
    a = int(input('Введите число - '))
while a < 0:
    break