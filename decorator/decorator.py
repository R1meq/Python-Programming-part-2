def log_arguments_to_file(fnc):
    count = 0

    def inner(*args):
        nonlocal count
        x = count = count + 1
        f = open("log.txt", "w")
        f.write(f"the {fnc.__name__} function is called {x} times")
        f.close()
        return fnc(*args)

    return inner

def to_tuple(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return tuple(result)

    return wrapper
