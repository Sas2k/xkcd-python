import random
import requests
import aiohttp

class xkcd:
    def __init__(self, aio=False, client=None) -> None:
        self.current = int(self._latest_comic()["num"])
        if aio:
            self.random = self._arandom
            self.get = self._aget
            self.latest_comic = self._alatest_comic
            self._client = client
        else:
            self.random = self._random
            self.get = self._get
            self.latest_comic = self._latest_comic
            
            if client:
                raise NotImplementedError
    
    def _random(self):
        comic_id = random.randint(1, self.current)
        random_comic = requests.get(f"https://xkcd.com/{comic_id}/info.0.json")
        return random_comic.json()

    def _get(self, id: int):
        comic = requests.get(f"https://xkcd.com/{id}/info.0.json")
        return comic.json()

    def _latest_comic(self):
        comic = requests.get(f"https://xkcd.com/info.0.json")
        return comic.json()
    
    async def _arandom(self):
        comic_id = random.randint(1, self.current)
        async with aiohttp.ClientSession() as client:
            async with client.get(f"https://xkcd.cocondam/{comic_id}/info.0.json") as random_comic:
                return await random_comic.json()
    
    async def _aget(self, id: int):
        async with aiohttp.ClientSession() as client:
            async with client.get(f"https://xkcd.com/{id}/info.0.json") as comic:
                return await comic.json()
   
    async def _alatest_comic(self):
        async with aiohttp.ClientSession() as client:
            async with client.get(f"https://xkcd.com/info.0.json") as latest_comic:
                return await latest_comic.json()
