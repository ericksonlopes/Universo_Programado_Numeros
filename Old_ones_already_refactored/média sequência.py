
lista = []  # Lista para o teste
contador = [num for num in range(2, 21)]  # Cria uma lista de 1 até 21

for num in contador:  # pega cada valor dentro da lista(contador)
    # inseri a sequencia de números em cada index da lista até o limite estabelecido
    lista.insert(num, [num for num in range(1, num)])
contador = 1
for seq in lista:  # imprime a sequencia que esta dentro de cada index da lista

    print(f'{contador:^2}', seq)
    contador += 1
print()  # só pra pular linha

lista_bruta = list(map(lambda dado: sum(dado) / len(dado), lista))
# lista_bruta = list(map(mean, lista))  # podemos utilizar a função mean para obter o mesmo resultado de cima

print(lista_bruta)  # imprime o valor médio de cada index da lista





