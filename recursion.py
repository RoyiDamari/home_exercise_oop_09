def range_like(from_, to_, incr):
    if from_ > to_:
        return
    print(from_)
    range_like(from_ + incr, to_, incr)


def factorial(n):

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def sum_of_digits(n):

    if n < 0:
        n = -n  # Convert negative numbers to positive
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)


def count_occurrences(lst, num):

    if not lst:  # Base case: if the list is empty, return 0
        return 0
    return (1 if lst[0] == num else 0) + count_occurrences(lst[1:], num)