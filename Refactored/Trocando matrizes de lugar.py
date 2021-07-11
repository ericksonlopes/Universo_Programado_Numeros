def matriz_mudar(index):
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    contador = 1
    while contador != 10:
        for linha in range(0, 3):
            for coluna in range(0, 3):
                matriz[linha][coluna] = contador
                contador += 1
    ind = []
    for linha in range(0, 3):
        for coluna in range(0, 3):
            if matriz[linha][coluna] == index:
                print(f'\033[33m[{matriz[linha][coluna]}]', end='')
                ind.append(linha)
                ind.append(coluna)
            else:
                print(f'\033[m[{matriz[linha][coluna]}]', end='')
        print()

    while True:  # parte que realiza os movimentos dentro da matriz
        letra = input('\033[mDigite a condição: ')
        if letra == 'sair':  # para finalizar o programa
            break
        # realiza o movimento da cor dentro da matriz
        if letra == 'w':
            x = ind[0]
            if x == 0:
                print('Limite alcançado! ')
            else:
                x = ind.pop(0)  # retira e retorna o número
                x -= 1  # subtrai 1 no valor
                ind.insert(0, x)  # coloca o novo valor dentro da lista no valor da linha
        if letra == 's':
            x = ind[0]
            if x == 2:
                print('Limite alcançado! ')
            else:
                x = ind.pop(0)
                x += 1
                ind.insert(0, x)
        if letra == 'a':
            x = ind[1]
            if x == 0:
                print('Limite alcançado')
            else:
                x = ind.pop(1)  # retira e retorna o valor
                x -= 1  # subtrai
                ind.insert(1, x)  # coloca o novo valor dentro da lista na coluna
        if letra == 'd':
            x = ind[1]
            if x == 2:
                print('Limite alcançar')
            else:
                x = ind.pop(1)
                x += 1
                ind.insert(1, x)

        # exibe a lista com os novos dados
        for l in range(0, 3):
            for c in range(0, 3):

                if (l == ind[0]) and (c == ind[1]):
                    print(f'\033[33m[{matriz[l][c]}]', end='')
                else:
                    print(f'\033[m[{matriz[l][c]}]', end='')

            print()
        print(f'\033[33mPosição atual{ind}\n')  # Informa a posição atual


inicio = int(input('Digite um número para começar: '))
print('w - subir\n'
      's - descer\n'
      'a - esquerda\n'
      'd - direita\n')
matriz_mudar(inicio)
