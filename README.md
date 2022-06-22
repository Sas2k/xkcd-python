# xkcd-python

xkcd-python is an API wrapper for xkcd.com written in python.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -U xkcd-python
```

## Usage

```python
from xkcd_python import *

#creates the client
client = Client()

# returns the comic by id
client.get(1)

# returns a random comic
client.random()

# returns the latest comic
client.latest_comic()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://github.com/Sas2k/xkcd-python/blob/main/LICENSE)