from configparser import ConfigParser

configure = ConfigParser()


def get(key: str, value: str, default: str = None):
    try:
        return configure.get(key, value)
    except Exception:
        return default


def getint(key: str, value: str, default: int = None):
    try:
        return configure.getint(key, value)
    except Exception:
        return default


def getfloat(key: str, value: str, default: float = None):
    try:
        return configure.getfloat(key, value)
    except Exception:
        return default
