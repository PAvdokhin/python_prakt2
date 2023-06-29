import time
a = int(input('Введите число - '))
if a > 0:
    time.sleep(a)
    a = int(input('Введите число - '))
else:
    print("Непредвиденная ошибка")
