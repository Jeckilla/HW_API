import requests


def smartest_hero(list_of_heroes: list):
    url = requests.get('https://akabab.github.io/superhero-api/api//all.json')
    file_info = url.json()
    list_heroes_int = []
    for name in file_info:
        if list_of_heroes.count(name['name']):
            list_heroes_int.append([name['powerstats']['intelligence'], name['name']])
    list_hero_sorted = sorted(list_heroes_int)
    return print(f'Самый умный супергерой {list_hero_sorted[-1][1]}')


smartest_hero(['Superman', 'Wonder Woman', 'Flash'])
