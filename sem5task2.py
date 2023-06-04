import collections
import json


with open("RomeoAndJuliet.json", "r", encoding="utf-8") as f:
    data = json.load(f)

f = collections.defaultdict(list)
for act in data["acts"]:
    for scene in act["scenes"]:
        for action in scene["action"]:
            for line in action["says"]:
                f[action["character"]].append(line)

with open('task5_2.json', 'w') as a:
    json.dump(f, a, ensure_ascii=False, indent=4)