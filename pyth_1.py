def Season(m):
    if m in (1, 2, 12):
        return "зима"
    elif m in (3, 4, 5):
        return "весна"
    elif m in (6, 7, 8):
        return "лето"
    elif m in (9, 10, 11):
        return "осень"


print(Season(int(input("Число месяца - "))))