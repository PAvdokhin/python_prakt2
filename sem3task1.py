import json
with open('task1.json', 'a+') as f:
    for line in open('wikidata_1000.json', 'r', encoding='utf-8'):
        data = json.loads(line)
        try:
            json.dump({data['label']['value']: data['description']['value']}, f, ensure_ascii=False, indent=4)
        except KeyError:
            json.dump({data['label']['value']: None}, f, ensure_ascii=False, indent=4)


#for item in data:
    ##print(a)

