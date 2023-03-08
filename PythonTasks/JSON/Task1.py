"""
Выведите из файла character.json Имя персонажа,родную планету и список эпизодов в которых он появлялся.
"""
# import json
# import re
#
#
# def printinfo(path):
#     with open(path, 'r+') as f:
#         data = f.read()
#     json_string = json.loads(data)
#
#     print(json_string['name'] + '\n' + json_string['origin']['name'])
#
#
#     print(f'Эпизоды с участием:')
#
#     for i in json_string["episode"]:
#         match = re.findall(r'\d+', i)
#         print(match[0])
#
#
# printinfo('character.json')

import json

with open("character.json", "r") as dead:
    data = json.load(dead)
def char(name,planet):
    print(
        f"Имя персонажа - {name}, родная планета: {planet} \n эпизоды: ")
    for i in data["episode"]:
        print(f"- {i}")

name = data["name"]
planet = data["origin"]["name"]

char(name, planet)