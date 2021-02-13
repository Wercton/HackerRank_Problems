if __name__ == '__main__':
    n = int(input())
    weird = "Weird"
    not_weird = "Not Weird"
    if n % 2:
        print(weird)
    else:
        if n < 5:
            print(not_weird)
        elif n <= 20:
            print(weird)
        else:
            print(not_weird)