import requests
from pprint import pprint

data = requests.get('https://blaze.com/api/roulette_games/recent').json()

# pprint(data[0]['color'])
# pprint(data[0]['roll'])

spins = [[item['color'], item['roll']] for item in data]
# pprint(spins)

info = []

# print(spins[1])
# print(spins[1][0])
# print(spins[1][1])

for item in spins:
    if item[0] == 1:
        info.append(['red', 'white', item[1]])
    elif item[0] == 2:
        info.append(['black', 'white', item[1]])
    else:
        info.append(['white','black', item[1]])

pprint(info[:5])