def soma_algarismo(dado_recebido):
    def soma_alga(dado):
        # transforma os números que chegam em formado de string em inteiros, e coloca dentro de uma lista
        lista_numeros = list(map(lambda trans_num: int(trans_num),
                                 # retira os caracteres que não são números, equivale a lista
                                 # verificando se o caractere é do tipo numérico
                                 filter(lambda retira_num: retira_num.isnumeric(), str(dado))))
        # retorna a soma de cada elemento da lista
        return sum(lista_numeros)

    # variável usada para verificação
    final = soma_alga(dado_recebido)
    # enquanto final não for menor que 10, passa novamente sobre a função de soma
    while final >= 10:
        # tem que ser passada por string pois o código só aceita assim
        final = soma_alga(str(final))
    # se a variável final for menor que 10, contendo uma casa, é retornado o valor pela função
    return final


for numero in range(1, 10):
    lista_cinco = [cinco for cinco in range(5, 50, 5)]
    print(lista_cinco)
    multiplicacao = 5 - numero  # 4 3 2 1 0 -1 -2 -3 -4

    for c in range(1, 10):
        if numero < 5:
            print(c)
            resultadosub = (multiplicacao - lista_cinco[c]) * - 1
            print(f'{numero} x {c} = {numero * c}  {lista_cinco[c]:>2} - {multiplicacao:>2} = {resultadosub:<2}')
            multiplicacao += 5 - numero
    print()

# def mul_5(numero):
#     lista_cinco = [cinco for cinco in range(5, 50, 5)]
#
#     multiplicacao = 5 - numero
#     x = 5 - numero
#     for c in range(0, 9):
#         if numero < 5:
#             resultadosub = (multiplicacao - lista_cinco[c]) * -1
#             print(f'{numero} x {c + 1} ({lista_cinco[c]:^3} - {multiplicacao:^2}) = {resultadosub:^2}  > '
#                   f'{soma_algoritmo(resultadosub)}')
#             multiplicacao += x
#         if numero > 5:
#             resultadosub = (multiplicacao * - 1) + lista_cinco[c]
#             print(f'{numero} x {c + 1} ({lista_cinco[c]:^3} + {(multiplicacao * -1):^2}) = {resultadosub:^2}  > '
#                   f'{soma_algoritmo(resultadosub)}')
#             multiplicacao += x
#         if numero == 5:
#             print(f'{numero} x {c + 1} = {lista_cinco[c]:^2}')
#     print()
