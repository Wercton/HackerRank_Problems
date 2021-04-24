def maior_calice(matriz):
    soma = []
    for i in range(4):
        for u in range(4):
            soma.append(sum(matriz[i][u:u+3]) + matriz[i + 1][u + 1] + sum(matriz[i + 2][u:u+3]))
    print(max(soma))


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    maior_calice(arr)
