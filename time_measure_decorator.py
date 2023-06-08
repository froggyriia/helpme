from time import time
def time_measure(func: callable):
    def wrapper(*args, **kwargs):
        before_execute = time()
        result = func(*args, **kwargs)
        after_execute = time()
        print(f'{func.__name__} was called for {after_execute - before_execute}')
        return result
    return wrapper
def func(*args):  # *args - негранич кол-во аргументов **kwargs - неогр колво аргуеньов-ключей
    print(args)