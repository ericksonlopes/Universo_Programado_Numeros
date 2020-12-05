def soma_algarismo(dado_recebido):
    def soma_alga(dado):
        lista_numeros = list(map(lambda trans_num: int(trans_num),
                                 filter(lambda retira_num: retira_num.isnumeric(), str(dado))))
        return sum(lista_numeros)

    final = soma_alga(dado_recebido)
    while final >= 10:
        final = soma_alga(str(final))
    return final


for num in range(1, 10):
    [print(f'{num:^3} + {mult:^3} = {num * mult:3} ({soma_algarismo(num * mult):^3})  ', end='')
     for mult in range(1, 10)], print()

print()

for num in range(1, 10):
    [print(f'{soma_algarismo(num * mult)} ', end=' ') for mult in range(1, 10)], print()

print()

for num in range(1, 10):
    [print(f'{num * mult:^3} ', end=' ') for mult in range(1, 10)], print()

