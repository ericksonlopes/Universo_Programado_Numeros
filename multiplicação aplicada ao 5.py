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


def mul_5(numero):
    lista_cinco = [cinco for cinco in range(5, 50, 5)]

    multiplicacao = 5 - numero
    x = 5 - numero
    for c in range(0, 9):
        if numero < 5:
            resultadosub = (multiplicacao - lista_cinco[c]) * -1
            print(f'{numero} x {c + 1} ({lista_cinco[c]:^3} - {multiplicacao:^2}) = {resultadosub:^2}  > '
                  f'{soma_algoritmo(resultadosub)}')
            multiplicacao += x
        if numero > 5:
            resultadosub = (multiplicacao * - 1) + lista_cinco[c]
            print(f'{numero} x {c + 1} ({lista_cinco[c]:^3} + {(multiplicacao * -1):^2}) = {resultadosub:^2}  > '
                  f'{soma_algoritmo(resultadosub)}')
            multiplicacao += x
        if numero == 5:
            print(f'{numero} x {c + 1} = {lista_cinco[c]:^2}')
    print()


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list(map(mul_5, lista))
