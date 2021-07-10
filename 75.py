def soma_algarismo(dado_recebido):
    def soma_alga(dado):
        lista_numeros = list(map(lambda trans_num: int(trans_num),
                                 filter(lambda retira_num: retira_num.isnumeric(), str(dado))))
        return sum(lista_numeros)

    final = soma_alga(dado_recebido)
    while final >= 10:
        final = soma_alga(str(final))
    return final


num = 20

# for x in range(1, 11):
#     for item in range(1, 20):
#         mult = item * x
#
#         print(f"{mult:>3} {soma_algarismo(mult)}")
#     print()

with open('75.txt', 'w') as arquivo:
    for item in range(1, 20):
        mult = item * 75

        print(f"{mult:>3} {soma_algarismo(mult)}", file=arquivo)

# 75(75)
# 150(75 + 75)
# 225(75 + 75 + 75)
#
# 75 = 75 * 1
# 150 = 75 * 2
# 225 = 75 * 3
