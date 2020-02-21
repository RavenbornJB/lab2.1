import math


def find_trimorph(num):
    """ int -> bool
    Determines if a number is a trimorph number.
    """
    return (num**3) % (10**5) == num


def find_products(lst):
    """ list -> list
    Returns a list of all possible products of numbers in a list
    except for products of identical numbers (a.k.a squares)
    """
    products = []
    for num1 in lst:
        for num2 in lst:
            prod = num1 * num2
            if not num1 == num2 and is_ascending(prod):
                products.append(prod)
    return list(set(products))


def is_ascending(num):
    """ int -> bool
    Determines if a number's digits are in an ascending order.
    """
    digits = list(str(num))
    return digits == sorted(digits)


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


def trimorph_process():
    lst1 = list(filter(find_trimorph, range(10**4, 10**5)))
    lst2 = find_products(lst1)
    top = max(lst2)
    return top, square_sum(top)