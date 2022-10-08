from . import *
import types


def imports():
    for name, val in globals().items():
        if isinstance(val, types.ModuleType):
            if '.' not in val.__name__ and 'types' not in val.__name__:
                name = val.__name__
                __import__('settings.models.' + name.capitalize())


imports()
