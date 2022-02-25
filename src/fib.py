from functools import lru_cache


@lru_cache(maxsize=1024)
def fib(n):
    """
    Fibonacci sequence, using python lru cache
    :param n:  the index of the n-th element in the Fibonacci sequence
    :type n: int
    :return:  the n-th element in the Fibonacci sequence
    :rtype int
    """
    if n == 1:
        return 1
    if n == 0:
        return 0
    else:
        return fib(n-1) + fib(n-2)
    

def mem_fib(n, cache=None):
    """
    Fibonacci sequence dynamic programming memoization (caching) approach
    :param n: the index of the n-th element in the Fibonacci sequence
    :param cache:
    :return: the n-th element in the Fibonacci sequence
    :rtype: int
    """
    if n == 0:
        return 0
    if n == 1:
        return 1

    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]

    result = mem_fib(n - 1, cache) + mem_fib(n - 2, cache)
    cache[n] = result
    return result


def dp_fib(n):
    """
    Fibonacci sequence dynamic programming bottom up approach
    :param n: the index of the n-th element in the Fibonacci sequence
    :return: the n-th element in the Fibonacci sequence
    :rtype: int
    """
    a = 1  # f(i - 2)
    b = 1  # f(i - 1)
    for i in range(2, n + 1):  # end of range is exclusive
        a, b = b, a + b
    return b


if __name__ == '__main__':
    print(fib(3))
