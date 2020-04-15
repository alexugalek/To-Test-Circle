from random import randint


def function_attempt(call_attempt):

    class ToManyErrors(Exception):

        def __init__(self, func_name):
            self.func_name = func_name

        def __str__(self):
            return '{} raised to many errors'.format(self.func_name)

    def outer(func):
        def wrapper(*args, **kwargs):
            for attempt_num in range(1, call_attempt + 1):
                try:
                    print('{} - {} attempt'.format(func.__name__, attempt_num))
                    result = func(*args, **kwargs)
                    print(
                        '{} - {} attempt was success'.format(
                            func.__name__, attempt_num
                        )
                    )
                    return result
                except Exception:
                    pass
            raise ToManyErrors(func.__name__)
        return wrapper
    return outer


@function_attempt(2)
def func1():
    """Function to check decorator

    :return: float
    """
    a = randint(-1, 1)
    print(a)
    return 100 / a


print(func1())
