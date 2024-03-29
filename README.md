# xkcd-python

![PYPI weekly Downloads](https://img.shields.io/pypi/dw/xkcd-python?style=for-the-badge)
![PYPI monthly Downloads](https://img.shields.io/pypi/dm/xkcd-python?style=for-the-badge)

xkcd-python is an API wrapper for xkcd.com written in python.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install xkcd-python.

```bash
pip install -U xkcd-python
```

## Usage

### Normal usage

```python
from xkcd_python import Client

#creates the client
client = Client()

# returns the comic by id
client.get(1)

# returns a random comic
client.random()

# returns the latest comic
client.latest_comic()
```

### Async usage

```python
from xkcd_python import Client
import asyncio

client = Client()

async def main():
    tasks = (client.get(x) for x in range(1, 20))
    return await asyncio.gather(*tasks)

asyncio.run(main)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://github.com/Sas2k/xkcd-python/blob/main/LICENSE)

