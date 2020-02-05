def find_automorphs():
    automorphs = []
    for num in range(10**5, 10**6):
        if (num**2) % (10**6) == num:
            automorphs.append(num)
    return automorphs


def find_products(lst):
    products = set()
    for num1 in lst:
        for num2 in lst:
            prod = num1 * num2
            if not num1 == num2 and not is_lischrel(prod):
                products.add(prod)
    return products


def is_lischrel(num):
    rev = int(str(num)[::-1])
    num_sum = num + rev
    if not str(num_sum) == str(num_sum)[::-1]:
        return True
    return False


def divisors(num):
    divs = set()
    for i in range(1, int(num**0.5) + 1):
        j = num / i
        if j % 1 == 0.0:
            divs.add((i, int(j)))
    return divs


if __name__ == "__main__":
    lst1 = find_automorphs()
    lst2 = find_products(lst1)
    top = max(lst2)
    print(top, divisors(top))