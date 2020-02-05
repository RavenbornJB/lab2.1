def find_leyland():
    leylands = []
    for i in range(2, int(10**2.5) + 1):
        for j in range(i, int(10**2.5) + 1):
            num = i**j + j**i
            if 10**4 <= num < 10**5:
                leylands.append(num)
    return leylands


def find_products(lst):
    products = set()
    for num1 in lst:
        for num2 in lst:
            prod = num1 * num2
            if not num1 == num2 and not is_palindrome(prod):
                products.add(prod)
    return products


def is_palindrome(num):
    num = str(num)
    return num == num[::-1]


def divisors(num):
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