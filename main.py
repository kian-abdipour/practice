def counting(number):
    yield number

    yield number

    yield number + 1

    return number


for num in counting(5):
    print(num)

