import json
with open('task2.json', 'r', encoding='utf-8'):
    with open('RomeoAndJuliet.json', 'a+', encoding='utf-8') as f:
        data = json.load(f)

print(data)
