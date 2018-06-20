# coding: utf8
import collections
import functools
import inspect

def check(func):
    msg = ('Expected type {expected!r} for argument {argument}, '
           'but got type {got!r} with value {value!r}')
    # To get defined parameters
    sig = inspect.signature(func)
    parameters = sig.parameters
    arg_keys = tuple(parameters.keys())

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        CheckItem = collections.namedtuple('CheckItem', ('anno', 'arg_name', 'value'))
        check_list = []

        # collect args
        for i, value in enumerate(args):
            arg_name = arg_keys[i]
            anno = parameters[arg_name].annotation
            check_list.append(CheckItem(anno, arg_name, value))

        # collect kwargs
        for arg_name, value in kwargs.items():
            anno = parameters[arg_name].annotation
            check_list.append(CheckItem(anno, arg_name, value))

        #check type
        for item in check_list:
            if not isinstance(item.value, item.anno):
                error = msg.format(expected=item.anno, argument=item.arg_name,
                                   got=type(item.value), value=item.value)
                raise TypeError(error)
        return func(*args, **kwargs)

    return wrapper

@check
def foobar(a: int, b: str, c: float = 3.2) -> tuple:
    return a, b, c