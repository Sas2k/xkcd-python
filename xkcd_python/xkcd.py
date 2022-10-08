import random
import requests

class xkcd:
    def __init__(self, async=False, client=None) -> None:
        self.current = int(latest_comic_id.json()["num"])
        if async:
            self.random = self._arandom
            self.get = self._aget
            self.latest_comic = self._alatest_comic
            self._client = client
            
            self.__aenter__ = self.enter
            self.__aexit__ = self.exit
        else:
            self.random = self._random
            self.get = self._get
            self.latest_comic = self._latest_comic
            
            if client:
                raise NotImplementedError
    
    async def enter(self):
        self._client = aiohttp.ClientSession()
        return self
    
    async def exit(self):
        await self._client.close()
    
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
        client = self.client if self.client else aiohttp.ClientSession()
        comic_id = random.randint(1, self.current)
        async with client.get(f"https://xkcd.com/{comic_id}/info.0.json") as random_comic:
            return await random_comic.json()
    
    async def _aget(self, id: int):
        client = self.client if self.client else aiohttp.ClientSession()
        comic_id = random.randint(1, self.current)
        async with client.get(f"https://xkcd.com/{id}/info.0.json") as comic:
            return await comic.json()
   
    async def _alatest_comic(self):
        client = self.client if self.client else aiohttp.ClientSession()
        comic_id = random.randint(1, self.current)
        async with client.get(f"https://xkcd.com/info.0.json") as latest_comic:
            return await latest_comic.json()
