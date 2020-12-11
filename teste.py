def soma_algarismo(dado_recebido):
    def soma_alga(dado):
        lista_numeros = list(map(lambda trans_num: int(trans_num),
                                 filter(lambda retira_num: retira_num.isnumeric(), str(dado))))
        return sum(lista_numeros)

    final = soma_alga(dado_recebido)
    while final >= 10:
        final = soma_alga(str(final))
    return final


def test():
    for num in range(1, 10):
        div = 360 / num
        print(num, div, soma_algarismo(div))

    print(360 / 7)

    [print(f'{i} {l}') for i, l in enumerate(list(range(n)) for n in range(0, 15))]

    print([i + sum(l) for i, l in enumerate(list(range(n)) for n in range(0, 15))])


num = 9

for x in range(1, 10):
    for y in range(1, 10):
        print(f'{x} x {y} = {x * y:^3}({soma_algarismo(x * y)}) | {(x * y) / num:^5}({soma_algarismo((x * y) / num)})')
    print()

# for x in range(1, 10):
#     [
#         print(f'{x} x {y} = {x * y:^3}({soma_algarismo(x * y)}) |
#         {(x * y) / num:^5}({soma_algarismo((x * y) / num)})')
#     for y in range[1, 10]],print()

# 1 1
# 2 5
# 3 369
# 4 7
# 5 2
# 6 369
# 7 ele mesmo/somente 7
# 8 8
# 9 resultados por 9
