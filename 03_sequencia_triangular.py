lista = []

for num in range(0, 15):

    lista_cont = [n for n in range(1, num+1)]
    print(f'{num:^3}', f'{str(lista_cont):^47}')
    lista.append(sum(lista_cont) + num)

print('\n ', lista)

print([i+sum(l) for i, l in enumerate(list(range(n)) for n in range(0, 15))])
