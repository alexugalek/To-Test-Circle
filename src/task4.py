def maximum_of_euler_function(n):
    """Fast counting maximum of i/f(i) where f - Euler function and i <= n

    Raise TypeError if n < 1 or n not integer
    :param n: natural number >= 1
    :return: tuple (i, f(i)), i - first number from sequence
    """

    def euler_func(number):
        """Fast counting of Euler function

        :param number: natural number
        :return: Euler f(n) result
        """

        value = number
        i = 2
        while i * i <= number:
            if number % i == 0:
                while number % i == 0:
                    number /= i
                value -= value / i
            i += 1
        if number > 1:
            value -= value / number
        return int(value)

    if n == 1:
        return 1, 1
    if n < 1 or not isinstance(n, int):
        raise TypeError

    lst_of_simple = []
    result = 1
    for i in range(2, n + 1):
        if result * i > n:
            break
        for j in lst_of_simple:
            if i % j == 0:
                break
        else:
            lst_of_simple.append(i)
            result *= i

    # this path of algorithm generate list of all numbers
    # where i/f(i) has maximum value
    index = 1
    lst_of_results = []
    while result * index < n:
        lst_of_results.append(result * index)
        index += 1

    return result, euler_func(result)


if __name__ == '__main__':
    print(maximum_of_euler_function(-1))
    print(maximum_of_euler_function(1000000))
