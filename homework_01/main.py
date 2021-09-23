"""
Домашнее задание №1
Функции и структуры данных
"""

from operator import pow, mod
from time import time_ns
from functools import wraps


def trace_and_time_call(indent: str = "____"):
    """
    Декоратор для вывода трассировки вызовов (удобно для рекурсивных функций)
    и времени выполнения функции
    """
    def trace_and_time_call_decorator(func):
        func.indent_level = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time_ns()
            args_str = ", ".join(map(repr, args))
            kwargs_str = ", ".join(map(lambda t: f"{t[0]}={t[1]!r}", kwargs.items()))
            func_args_str = ", ".join(list(filter(bool, (args_str, kwargs_str))))
            print(indent * func.indent_level, f">>> {func.__name__}({func_args_str})")
            func.indent_level += 1
            result = func(*args, **kwargs)
            func.indent_level -= 1
            time_taken = (time_ns() - start_time) / 1_000_000
            print(
                indent * func.indent_level,
                f"<<< {func.__name__}({func_args_str}) => {result}",
                f" Elapsed: {time_taken:.3f} ms"
            )
            return result
        return wrapper
    return trace_and_time_call_decorator


@trace_and_time_call()
def power_numbers(*nums, pwr: int = 2) -> list:
    """
    Функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    (степень числа также можно задать через дополнительный аргумент pwr)
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    >>> power_numbers(1, 2, 5, 7, pwr=3)
    <<< [1, 8, 125, 343]
    """
    return list(map(pow, nums, [pwr] * len(nums)))


# @trace_and_time_call()
def is_prime(num: int) -> bool:
    """
    Функция проверки, является ли число простым или нет
    """
    if (num <= 1):
        return False
    elif (num <= 3):
        return True
    elif ((num % 2) == 0 or (num % 3) == 0):
        return False
    i = 5
    while(pow(i, 2) <= num):
        if ((num % i) == 0 or (num % (i + 2)) == 0):
            return False
        i = i + 6
    return True


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


@trace_and_time_call()
def filter_numbers(nums, fltr=ODD) -> list:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только нечётные/чётные/простые числа
    (выбор производится передачей дополнительного аргумента fltr)
    >>> filter_numbers([1, 2, 3])
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    >>> filter_numbers([3, 4, 5, 6, 7], PRIME)
    <<< [3, 5, 7]
    """
    if nums is None:
        nums = []
    if (fltr == ODD):
        return list(filter((lambda x: mod(x, 2) != 0), nums))
    elif (fltr == EVEN):
        return list(filter((lambda x: mod(x, 2) == 0), nums))
    elif (fltr == PRIME):
        return list(filter(is_prime, nums))
    else:
        return nums


@trace_and_time_call("--")
def fib(n: int) -> int:
    """
    Функция вычисления n-ого элемента последовательности Фибоначчи
    """
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":

    test_nums = [i + 1 for i in range(10)]
    test_nums_power_2 = power_numbers(*test_nums)
    test_nums_power_3 = power_numbers(*test_nums, pwr=3)
    test_nums_power_4 = power_numbers(*test_nums, pwr=4)
    print("num\tpow2\tpow3\tpow4")
    for i in range(len(test_nums)):
        print(f"{test_nums[i]}\t{test_nums_power_2[i]}\t{test_nums_power_3[i]}\t{test_nums_power_4[i]}")
    print()
    test_nums = [i + 1 for i in range(30)]
    test_odd_nums = filter_numbers(test_nums)
    test_even_nums = filter_numbers(test_nums, EVEN)
    test_prime_nums = filter_numbers(test_nums, fltr=PRIME)
    print("List of numbers:", test_nums)
    print("- contains odd numbers:", test_odd_nums)
    print("- contains even numbers:", test_even_nums)
    print("- contains prime numbers:", test_prime_nums)
    print()
    fib_seq_len = 7
    print(f"Fibonacci sequence (first {fib_seq_len} terms):", [fib(i) for i in range(fib_seq_len)])
