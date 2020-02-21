import math


def find_leyland():
    """ None -> list
    Returns a list of all leyland numbers between 10000 and 100000
    """
    leylands = []
    for i in range(2, int(math.log2(100000))):
        for j in range(2, int(math.log2(100000))):
            num = i**j + j**i
            if 10**4 <= num < 10**5:
                leylands.append(num)
    return leylands


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


def divisors(num):
    """ int -> list
    Returns a list of tuples which contain two numbers each.
    The two numbers in each tuple, when multiplied together,
    equate to the input number.
    """
    divs = set()
    for i in range(1, int(num**0.5) + 1):
        j = num / i
        if j % 1 == 0.0:
            divs.add((i, int(j)))
    return divs


if __name__ == "__main__":
    lst1 = find_leyland()
    lst2 = find_products(lst1)
    top = max(lst2)
    print(top, divisors(top))