def soma_algarismo(numero):
    while not numero < 10:
        numero = sum(list(map(lambda x: int(x), [num for num in str(numero)])))
    return numero


lista = [[num_m for num_m in range(0, num*10, num) if not num_m == 0] for num in range(1, 10)]

for multi in lista:
    for num in range(len(multi)):
        if soma_algarismo(multi[num]) in [1, 2, 4, 8, 5, 7]:
            print('\033[33m' + f'{soma_algarismo(multi[num]): ^3} ', end='')
        else:
            print('\033[34m'+f'{soma_algarismo(multi[num]): ^3} ', end='')
    else:
        print('    ', end='')
        for num in range(len(multi)):
            if soma_algarismo(multi[num]) in [1, 2, 4, 8, 5, 7]:
                print('\033[33m' + f'{multi[num]: ^3} ', end='')
            else:
                print('\033[34m' + f'{multi[num]: ^3} ', end='')
    print()

print()
print()

for multi in lista:
    for num in range(len(multi)):
        if soma_algarismo(multi[num]) in [3, 6, 9]:
            print('\033[33m' + f'{soma_algarismo(multi[num]): ^3} ', end='')
        else:
            print('\033[34m'+f'{soma_algarismo(multi[num]): ^3} ', end='')
    else:
        print('    ', end='')
        for num in range(len(multi)):
            if soma_algarismo(multi[num]) in [3, 6, 9]:
                print('\033[33m' + f'{multi[num]: ^3} ', end='')
            else:
                print('\033[34m' + f'{multi[num]: ^3} ', end='')
    print()









