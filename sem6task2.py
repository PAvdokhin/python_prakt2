import time

st = time.time()


def number_is_even(n):
    return n % 2 == 0


a = number_is_even(310284)
b = number_is_even(2104)
c = number_is_even(102001)
d = number_is_even(10029481)
end = time.time()
delta = st - end
print(delta)


file = f"sem6task2(1){time.strftime('%d.%m.%Y')}.txt"
with open (file, 'w') as f:
    f.write(f"Время выполнения операции: {delta} секунд")