import logging


def log_arguments_to_file(fnc):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        x = count = count + 1
        f = open("log.txt", "w")
        f.write(f"the {fnc.__name__} function is called {x} times")
        f.close()
        return fnc(*args, **kwargs)

    return inner


def to_tuple(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return tuple(result)

    return wrapper


def logged(custom_exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except custom_exception as e:
                if mode == "console":
                    logging.basicConfig(level=logging.INFO)
                    logging.error(e)
                elif mode == "file":
                    logging.basicConfig(filename="exception.log", level=logging.INFO)
                    logging.error(e)
                else:
                    raise ValueError("Invalid mode")
        return wrapper
    return decorator
