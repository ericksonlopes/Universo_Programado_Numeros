def soma_algarismo(dado_recebido):
    def soma_alga(dado):
        lista_numeros = list(map(lambda trans_num: int(trans_num),
                                 filter(lambda retira_num: retira_num.isnumeric(), str(dado))))
        return sum(lista_numeros)

    final = soma_alga(dado_recebido)
    while final >= 10:
        final = soma_alga(str(final))
    return final


# for para percorrer os 9 numeros
for num in range(1, 10):
    if num != 7:
        # variavel com a quantidade de graus de uma circuferencia
        circulo_graus = 360

        # divide a quatidade de graus pelo numero da vez
        div = int(circulo_graus / num)

        print(f'[{"Subtração":^11}]', f'[{"Resultado":^6}]',
              f'[{"soma do algarismo":^5}]', f'[{num} / {390} = {int(360 / num)}]')

        while circulo_graus >= 0:
            print(f'[{str(circulo_graus) + "-" + str(div):^11}]',
                  f'[{circulo_graus:^9}]', f'[{soma_algarismo(circulo_graus):^17}]')
            circulo_graus = circulo_graus - div
        print()

    else:
        print('O número 7, não entra de acordo por sua divizão '
              f'ser uma dizima periodica com o resultado equivalente a: {360 / 7} \n')
