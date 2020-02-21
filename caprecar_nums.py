import math


def find_caprecar(num):
    """ int -> bool
    Determines if a number is Kaprekar (by definition from the test)
    """
    square = str(num ** 2)
    for i in range(1, len(square)):
        left, right = int(square[:i]), square[i:]
        while right.startswith('0'):
            right = right[1:]
        total = left + int(right) if right.isdigit() else left
        if total == num:
            return True
    return False


def find_products(lst):
    """ list -> list
    Returns a list of all possible products of numbers in a list
    except for products of identical numbers (a.k.a squares)
    """
    products = set()
    for num1 in lst:
        for num2 in lst:
            prod = num1 * num2
            if not num1 == num2 and not is_palindrome(prod):
                products.add(prod)
    return products


def is_palindrome(num):
    """ int -> bool
    Determines if a number is a palindrome
    """
    num = str(num)
    return num == num[::-1]


def square_sum(num):
    """ int -> list
    Returns a list of tuples which contain two numbers each.
    The two numbers in each tuple, when squared and added together,
    equate to the input number.
    """
    components = []
    squares = {i**2: i for i in range(int(math.sqrt(num)) + 1)}
    for square in squares:
        if num - square in squares:
            components.append((squares[square], squares[num - square]))
    return components


def caprecar_process():
    lst1 = list(filter(find_caprecar, range(10**3, 10**4)))
    lst2 = find_products(lst1)
    top = min(lst2)
    return top, square_sum(top)