# This is a decorator that get the function and print the name of function then call the function
# Actually, this is use for show where is user, and now it is in witch tab
def representing(func):
    def inner(*args, **kwargs):
        print("\n*_*", func.__name__, "tab", "\n")
        value_for_returning = func(*args, **kwargs)

        return value_for_returning

    return inner

