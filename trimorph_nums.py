import math


def find_trimorphs():
    trimorphs = []
    for num in range(10**4, 10**5):
        if (num**3) % (10**5) == num:
            trimorphs.append(num)
    return trimorphs


def find_products(lst):
    products = []
    for num1 in lst:
        for num2 in lst:
            prod = num1 * num2
            if not num1 == num2 and is_ascending(prod):
                products.append(prod)
    return list(set(products))


def is_ascending(num):
    digits = list(str(num))
    return digits == sorted(digits)


def square_sum(num):
    components = []
    squares = {i**2: i for i in range(int(math.sqrt(num)) + 1)}
    for square in squares:
        if num - square in squares:
            components.append((squares[square], squares[num - square]))
    return components


if __name__ == "__main__":
    lst1 = find_trimorphs()
    lst2 = find_products(lst1)
    top = max(lst2)
    lst3 = square_sum(top)
    print(top, lst3)