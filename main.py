from recursion import range_like, factorial, sum_of_digits, count_occurrences
from files_system import draw_files_system


def main():

    # range recursion
    print("range recursion")
    range_like(1, 30, 3)
    print("-" * 50)

    # factorial recursion
    print("factorial recursion")
    try:
        print(factorial(-1))
    except ValueError as e:
        print(f"Value Error: {e}")
    print(factorial(5))
    print("-" * 50)

    # sum of digit recursion
    print("sum of digit recursion")
    print(sum_of_digits(86))
    print(sum_of_digits(404))
    print(sum_of_digits(0))
    print(sum_of_digits(-75))
    print("-" * 50)

    # count_occurrences
    print("count_occurrences")
    print(count_occurrences([1, 2, 2, 3, 2, 4], 2))
    print(count_occurrences([5, 5, 5, 5], 5))
    print(count_occurrences([1, 2, 3, 4], 6))
    print(count_occurrences([], 10))

    draw_files_system("C:/Git")



if __name__ == "__main__":
    main()