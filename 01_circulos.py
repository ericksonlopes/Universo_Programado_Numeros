# autor: Erickson Lopes


def soma_algoritmo(c):
    soma = 0
    n = int(str(c).replace(".", ""))
    while n > 0:
        resto = n % 10
        n = n // 10
        soma = soma + resto
        if soma >= 10:
            resto = soma % 10
            soma = soma // 10
            soma = soma + resto
    return soma


def circulo_numero(num):
    if num != 7:  # Verifica se é 7
        circulo = 360  # circuferencia completa
        div = circulo / num  # Divide o número por 360 e gera divisão

        print(f'{num} dividido {circulo} igual {int(div)}(A sequência subtrai a partir dele)')

        contador = 1
        print(f'[{"subtração":^5}]', f'[{"soma da subtração":^5}]')
        while circulo >= 0:
            if circulo == 0:
                print(f'[{int(circulo):^9}]')
            else:
                print(f'[{int(circulo):^9}]', f'[{soma_algoritmo(circulo):^5}]')
            circulo = circulo - div  # subtrai a cada laço pelo número(variavel da vez)
            contador += 1
        print()

    else:
        print('O número 7 não é capaz de ser introduzido, por ser o unico número \n'
              'que na subtração do resultado da divisão não chega a 0\n'
              '360 dividido por 7 é igual 51.42857142857143.')
        print()


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list(map(circulo_numero, lista))

# mult_5 = lambda num=5: [print(f'[{num:^3} x {mult:^3}] = {num * mult:^4}'
#                               f' {soma_algoritmo(num * mult)}') for mult in range(1, 10)]
# mult_5()
#
# print()


# num = int(input("Digite um número: "))
# circulo = 360
# div = circulo / num
#
# print(f'{num} dividido por {circulo} é igual a {div}')
#
# contador = 1
# while contador != 9:
#     circulo = circulo - div
#     print(circulo)
#     contador += 1
#     if circulo == 0:
#         break

