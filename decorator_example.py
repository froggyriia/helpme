from  time import time, sleep
def double(func):
    def wrapper(*args, **kwargs):
        return func(*args, ** kwargs) * 2

    return wrapper




@double
def sum(a, b):
    return a + b

@time_measure

def mult(a, b):
    sleep(1)
    return a * b


@double
def sub(a, b):
    return a - b


def father(x):
    def inside(repeat: int):
        print(x * repeat)

    return inside


# first = father('hi')
# second = father('bly')
# first(1)
# second(2)
