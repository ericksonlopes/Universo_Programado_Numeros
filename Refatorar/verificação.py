listaP = [1, 2, 4, 8, 7, 5]
listaS = [3, 6, 9]

t1 = 1
t2 = 1
t3 = t1 + t2
t4 = t3

numero = int(input('insira um numero de no maxímo dois digitos:'))  # Pega o valor em int

if numero < 10:
    if numero in listaP:  # Procura o valor da variavel dentro da lista
        print('1, 2, 4, 8, 7, 5')

    elif numero in listaS:  # Caso a primeria seja 'False', realiza essa verificação com a segunda lista
        print('3, 6, 9')
else:
    print('0')
