import time


def decorator_function(func):
    def wrapper(*args, **kwargs):
        print(f'wrapper run before {func.__name__} run')
        func(*args, **kwargs)
    return wrapper


def time_traking(func):
    '''Practice with time tracking'''
    def wrapper(*args, **kwargs):
        then = time.time()
        result = func(*args, **kwargs)
        now = time.time()
        print(f'{func.__name__} took {now - then}s for executing.')
        return result
    return wrapper


@time_traking
def print_something(msg):
    time.sleep(1)
    return msg


print(print_something('hello world'))
