from xkcd_python import __version__, __author__


def test_version():
    assert __version__ == '0.1.0'

def test_author():
    assert __author__ == "Sasen Perera"