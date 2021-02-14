if __name__ == '__main__':
    p = [input() for _ in range(int(input()))]
    for word in p:
        print("".join(word[::2]), "".join(word[1::2]))