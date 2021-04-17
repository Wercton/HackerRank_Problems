def factorial(number):
    if not number or number == 1:
        return 1
    if number > 1:
        return number * factorial(number-1)


if __name__ == '__main__':
    result = factorial(int(input()))
    print(result)
