import urllib.request
import json


craft = {}
astronaut = []
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)

with response as url:
    data = json.loads(url.read().decode())
    print(f"There are {data['number']} people in space right now.")
    for people in data['people']:
        astronaut.append(people)

for i in range(len(astronaut)):
    craft[astronaut[i]['name']]= astronaut[i]['craft']

# :<20
# < left aligned
# 20 total size of 'cell'

print('{:<20}|{:<10}'.format('Name','Craft'))
print('{:<20}|{:<10}'.format('-'*20,'-'*5))

for name,craft in sorted(craft.items()):
    print('{:<20}|{:<10}'.format(name,craft))
