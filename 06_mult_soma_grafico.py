import matplotlib.pyplot as pl


def soma_algarismo(dado_recebido):
    def soma_alga(dado):
        lista_numeros = list(map(lambda trans_num: int(trans_num),
                                 filter(lambda retira_num: retira_num.isnumeric(), str(dado))))
        return sum(lista_numeros)

    final = soma_alga(dado_recebido)
    while final >= 10:
        final = soma_alga(str(final))
    return final


lista = []

for item in [1, 2, 4, 8, 7, 5]:
    lista.append([soma_algarismo(num) for num in range(item, item * 10, item)])

y = [num for num in range(1, 10)]

for result in lista:
    pl.plot(result, y)

pl.show()
