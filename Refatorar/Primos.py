from math import sqrt


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


print("Primos: 2")
primos, limite = [2], 100

for numero in range(3, limite + 1, 2):  # pula de dois em dois
    ehprimo = 1
    for i in primos:
        if numero % i == 0:
            ehprimo = 0
            break
        if i > sqrt(numero):
            break
    if ehprimo:
        primos.append(numero)
        print(numero, soma_algoritmo(numero))
