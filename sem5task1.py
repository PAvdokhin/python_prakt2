from collections import Counter
import json


with open("RomeoAndJuliet.json", "r", encoding="utf-8") as f:
    data = json.load(f)

words = []
for act in data["acts"]:
    for scene in act["scenes"]:
        for action in scene["action"]:
            for line in action["says"]:
                for word in line.split(' '):
                    words.append(word)

print("20 самых встречаемых слов: ", Counter(words).most_common(20))
print("20 наименее встречающихся слов: ", Counter(words).most_common()[:-20:-1])

