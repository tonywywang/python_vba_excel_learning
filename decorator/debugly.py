#debugly.py

from functools import wraps, partial

def debug(func = None, *, prefix = ''):
    if func is None:
        # func is not passed
        return partial(debug, prefix=prefix)

    msg = prefix + func.__qualname__

    @wraps(func)   #without wraps, there are somethings weird in decorated function, e.g. function.__qualname__ show wrapper name not its own name
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)
    return wrapper

def debugmethods(cls):
    #cls is a class
    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, debug(val))

    return cls
