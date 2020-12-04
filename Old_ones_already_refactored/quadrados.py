from math import sqrt


def fracoes_exatas(limite):
    def soma_numero(num):
        num = list(filter(lambda x: x.insnumeric(), num))
        return num

    for numero in range(limite):
        if len(str(sqrt(numero))) < 6:
            print(f'{numero:^3}, {sqrt(numero)}')
            # print(f'{numero:^3}, {soma_numero(numero)} {sqrt(numero)}')


fracoes_exatas(500)


def soma_numero(num):
    numero = sum(list(map(lambda num_int: int(num_int), list(filter(lambda s_numero: s_numero.isnumeric(), str(num))))))
    return numero


print(soma_numero('3u61250'))

for i in range(1, 100 + 1):
    s = i ** 2
    k = s + s
    a = s + s + s
    t = s + s + s + s
    e = s + t
    for n in range(1, 11):
        if n ** 2 > i + i - 1:
            break
    print(s, k, a, t, e)
