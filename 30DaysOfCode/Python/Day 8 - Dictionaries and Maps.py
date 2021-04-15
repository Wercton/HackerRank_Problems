if __name__ == '__main__':
    phone = {}
    for _ in range(int(input())):
        nome, numero = input().split()
        phone[nome] = numero
    while True:
        try:
            search = input()
            if search in phone.keys():
                print(f'{search}={phone[search]}')
            else:
                print('Not found')
        except EOFError:
            break

