def find_automorph(num):
    """ int -> bool
    Determines if a number is an automorph number
    """
    return (num**2) % (10**6) == num


def find_products(lst):
    """ list -> list
    Returns a list of all possible products of numbers in a list
    except for products of identical numbers (a.k.a squares)
    """
    products = set()
    for num1 in lst:
        for num2 in lst:
            prod = num1 * num2
            if not num1 == num2 and not is_lischrel(prod):
                products.add(prod)
    return products


def is_lischrel(num):
    """ int -> bool
    Determines if a number is a Lischrel number
    """
    rev = int(str(num)[::-1])
    num_sum = num + rev
    if not str(num_sum) == str(num_sum)[::-1]:
        return True
    return False


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


def lischrel_process():
    lst1 = list(filter(find_automorph, range(10**5, 10**6)))
    lst2 = find_products(lst1)
    top = max(lst2)
    return top, divisors(top)