def convert_binary(n):
    binary = ""
    while n > 0:
        rest = n % 2
        binary += str(rest)
        n = n // 2
    return count_consecutive(binary)


def count_consecutive(binary):
    maximum, count = 0, 0
    for i in binary:
        if i == "1":
            count += 1
            if maximum < count:
                maximum = count
        else:
            count = 0
    return maximum


if __name__ == '__main__':
    print(convert_binary(int(input())))
