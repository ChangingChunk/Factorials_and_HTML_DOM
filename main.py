def test(*args):
    print(*args)


def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n


test(1, True, 'Hi')
print(factorial(5))
