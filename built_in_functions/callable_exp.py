[x for x in dir(list) if callable(getattr(list, x))]
# [x for x in dir(list) if callable(x)] won't work since dir() returns string