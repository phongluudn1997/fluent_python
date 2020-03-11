def decorator_function(func):
    def wrapper(*args, **kwargs):
        print(f'wrapper run before {func.__name__} run')
        return func(*args, **kwargs)
    return wrapper


@decorator_function
def print_something(msg):
    print(msg)


print_something('hello world')
