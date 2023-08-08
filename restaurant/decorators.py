def representing(func):
    def inner(*args, **kwargs):
        print("\n*_*", func.__name__, "page", "\n")
        value_for_returning = func(*args, **kwargs)

        return value_for_returning

    return inner

