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


numerostr = str(input('Digite um número para obter sua sequência na multiplicação: '))
numero = int(str(numerostr).replace(".", ""))
print(soma_algoritmo(numero))

cont = 1
cont_final = 20  # com essa variavel voce pode mudar a quantidade de vezes que o resutlado aparece

if soma_algoritmo(numero) in [3, 6]:
    cont_final = 3
elif soma_algoritmo(numero) in [9]:
    cont_final = 2

while cont != cont_final:   # com essa variavel voce pode mudar a quantidade de vezes que o resutlado aparece
    tab = numero * cont
    print(f"{numero} X {cont} = {tab, soma_algoritmo(tab)}")

    if soma_algoritmo(tab) == 9:
        print('=' * 17)

    cont = cont + 1



