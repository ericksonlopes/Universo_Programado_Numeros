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
    div = 360 / num
    print(num ,div, soma_algarismo(div))


print(360 / 7)