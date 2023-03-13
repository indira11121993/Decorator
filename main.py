import requests
from decorator_2 import logger


@logger(path="log_info.txt")
def get_personage(id_personage):
    req = requests.get(f'https://swapi.dev/api/people/{id_personage}').json()
    for i in req:
        return i

print(get_personage(1))