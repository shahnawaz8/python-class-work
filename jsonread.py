import json
with open('d1.json') as file:
    data=json.load(file)
    for p in data['people']:
        print('name:'+p['name'])
        print('website:'+p['name'])
        print('from:'+p['name'])
    print()
        