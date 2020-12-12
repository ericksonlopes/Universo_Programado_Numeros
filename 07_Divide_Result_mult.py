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
    print(f'\n    Dividindo Resultado da Multiplicação Por: {num} ')
    for x in range(1, 10):
        [print(f'{x * y:>5}/{num} = {str((x * y) / num)[:6]:>6} ({soma_algarismo((x * y) / num)})', end='  ')
         for y in range(1, 10)], print()


# 1 | 1
# 2 | 5
# 3 | 3 6 9
# 4 | 7
# 5 | 2
# 6 | 3 6 9
# 7 | Apenas resultado de sua mult 7
# 8 | 8
# 9 | Apenas resultado de sua mult 9 - 3 6 9
