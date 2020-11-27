def escolher_num():
    numero = int(input("Digite um número: "))
    circulo = 360
    divi = circulo / numero

    print(f'{numero} dividido por {circulo} é igual a {divi}')

    contador = 1
    while contador != 9:
        circulo = circulo - divi
        print(circulo)
        contador += 1
        if circulo == 0:
            break


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
    # caso o numero não seja equivalente a 7
    if num != 7:
        # variavel com a quantidade de graus de uma circuferencia
        circulo_graus = 360

        # divide a circunferência  pelo numero da vez
        div = int(circulo_graus / num)

        # Exibe a conta da vez
        print(f'[{str(num) + " dividido por " + str(circulo_graus) + " é igual a " + str(div):^43}]')
        # Para simbolizar cada coluna
        print(f'[{"Subtração":^11}]', f'[{"Resultado":^6}]', f'[{"Soma do Algarismo":^5}]')

        # Caso o Resultado da operação ainda não seja menor ou igual a 0
        while circulo_graus >= 0:
            # Exibe os resultados informativos [ Subtração ] [Resultado] [soma do algarismo]
            print(f'[{str(circulo_graus) + "-" + str(div):^11}]',
                  f'[{circulo_graus:^9}]', f'[{soma_algarismo(circulo_graus):^17}]')

            # Subtrai a circuferencia antiga pela nova, adquirindo o resultado da divisão e
            # subtraindo pelo resultado da variavel circulo_graus atual
            circulo_graus = circulo_graus - div

        print()  # pula linha

    else:
        print('O número 7, não entra por conta de sua divisão '
              f'ser uma dizima periodica com o resultado equivalente a: {360 / 7} \n')
