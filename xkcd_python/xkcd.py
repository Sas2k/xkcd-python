from requests import *
from random import *

class xkcd():
    def __init__(self) -> None:
        pass

    def random(self = None):
        latest_comic_id = request("GET", "https://xkcd.com/info.0.json")
        comic_id = randint(1, int(latest_comic_id.json()["num"]))
        random_comic = request("GET", f"https://xkcd.com/{comic_id}/info.0.json")
        return random_comic.json()

    def get(id: int, self = None):
        comic = request("GET", f"https://xkcd.com/{id}/info.0.json")
        return comic.json()

    def latest_comic(self = None):
        comic = request("Get", f"https://xkcd.com/info.0.json")
        return comic.json