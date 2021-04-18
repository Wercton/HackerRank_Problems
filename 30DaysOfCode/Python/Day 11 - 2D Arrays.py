def maior_calice(matriz):
    soma = 0
    for i in range(4):
        for u in range(4):
            soma = matriz[i][u] + matriz[i][u + 1] + matriz[i][u + 2] + matriz[i + 1][u + 1] + matriz[i + 2][u] + \
                   matriz[i + 2][u + 1] + matriz[i + 2][u + 2]
            if i == 0 and u == 0:
                maior_soma = soma
            elif soma > maior_soma:
                maior_soma = soma
    print(maior_soma)


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    maior_calice(arr)
