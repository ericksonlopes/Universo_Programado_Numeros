def soma_algarismo(dado_recebido):
    def soma_alga(dado):
        lista_numeros = list(map(lambda trans_num: int(trans_num),
                                 filter(lambda retira_num: retira_num.isnumeric(), str(dado))))
        return sum(lista_numeros)

    final = soma_alga(dado_recebido)
    while final >= 10:
        final = soma_alga(str(final))
    return final


# num = 1

# for y in range(35):
#     x = num + 1
#     print(f'{x:>10} ({soma_algarismo(x)})', end=' ')
#     num = num + x
#     print(f'{num} {x}')


# for y in range(10):
#     print(num, end=' + ')
#     x = num + 1
#     print(f'{x:^2}', end=' = ')
#     num = soma_algarismo(num + x)
#     print(num)

# lista = []
# for num in range(1, 10):
#     lista_mult = []
#     for mult in range(1, 10):
#         lista_mult.append(num * mult)
#     lista.append(lista_mult)
#
# for mult in lista:
#     print(mult)


# a = [9, 5, 1, 6, 2, 7, 3, 8, 4]

# cont = 1
#
# while cont != 10:
#     print(cont, x[cont - 1])
#     cont += 1
#
# num = 1
# for y in range(10):
#     print(num, end=' + ')
#     x = num + 1
#     print(f'{x:^2}', end=' = ')
#     num = soma_algarismo(num + x)
#     print(num)


# x.index(9)

#
a = [9, 5, 1, 6, 2, 7, 3, 8, 4]

num = 1
for y in range(10):
    print(num, end=' + ')
    x = num + 1
    print(f'{x:^2}', end=' = ')
    num = soma_algarismo(num + x)
    print(num)


#  Primeiro commit do ano





