import xkcd_python
import unittest
import asyncio
import requests

async def _test_async(self):
    xkcd = xkcd_python.Client(aio=True)
    self.assertEqual((await xkcd.get(1))["num"], 1)
    self.assertEqual((await xkcd.latest_comic())["num"], self.get_latest())


class TestXkcd(unittest.TestCase):
    def get_latest(self):
        return requests.get("https://xkcd.com/info.0.json").json()["num"]

    def test_sync(self):
        xkcd = xkcd_python.Client()
        self.assertEqual(xkcd.get(1)["num"], 1)
        self.assertEqual(xkcd.latest_comic()["num"], self.get_latest())

    def test_async(self):
        asyncio.run(_test_async(self))

    def test_author(self):
        self.assertEqual(xkcd_python.__author__, "Sasen Perera")

if __name__ == "__main__":
    unittest.main()