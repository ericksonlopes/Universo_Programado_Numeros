from math import sqrt


def soma_algarismo(dado_recebido):
    def soma_alga(dado):
        lista_numeros = list(map(lambda trans_num: int(trans_num),
                                 filter(lambda retira_num: retira_num.isnumeric(), str(dado))))
        return sum(lista_numeros)

    final = soma_alga(dado_recebido)
    while final >= 10:
        final = soma_alga(str(final))
    return final


for num, pos in enumerate(range(1, 2000)):
    raiz = sqrt(num)
    if raiz == int(raiz):
        print(f"{pos:^5}", f"{soma_algarismo(pos)}", f"{raiz:^5}", f"{soma_algarismo(raiz):^5}")