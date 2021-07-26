def product(*num):
    result = 1
    for i in num:
        result *= i
    print(result)


product(10, 20, 30)


def sum(num1, *arg):
    result = 0
    for i in arg:
        result += i
    print(result)


sum(5000, 20, 30)
