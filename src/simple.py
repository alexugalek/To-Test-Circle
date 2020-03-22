import math


def check_simple(num):
    for divider in range(2, math.floor(num**0.5)):
        if not (num % divider):
            return False
    return True
