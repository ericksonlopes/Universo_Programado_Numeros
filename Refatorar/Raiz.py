from math import sqrt


def fracoes_exatas(limite):
    def soma_numero(num):
        num = list(filter(lambda x: x.insnumeric(), num))
        return num

    for numero in range(limite):
        if len(str(sqrt(numero))) < 6:
            print(f'{numero:^3}, {sqrt(numero)}')
            # print(f'{numero:^3}, {soma_numero(numero)} {sqrt(numero)}')


fracoes_exatas(100)


def soma_numero(num):
    numero = sum(list(map(lambda num_int: int(num_int), list(filter(lambda s_numero: s_numero.isnumeric(), str(num))))))
    return numero

print(soma_numero('3u61250'))
