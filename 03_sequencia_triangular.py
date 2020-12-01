lista = []

for num in range(1, 15):
    lista_cont = [n for n in range(1, num)]
    print(f'{num:^3}', f'{str(lista_cont):^47}')

    lista.append(sum(lista_cont) + num)

print('\n ', lista)

# for num in range(1, 15):
#     lista_cont = [n for n in range(1, num)]
#     print(f'{num:^3}', f'{str(lista_cont):^47}')
#
#     lista.append(sum(lista_cont) )
#
# print('\n ', lista)
