def soma_algoritmo(n):
    soma = 0
    while n > 0:
        resto = n % 10
        n = n // 10
        soma = soma + resto
        if soma >= 10:
            resto = soma % 10
            soma = soma // 10
            soma = soma + resto
    return soma


#
#
# m = int(input('Some um algarismo: '))
# print(soma_algoritmo(m))

m = 1
z = 3
e = 5
t = 7
for i in range(1, 10):
    print(f'({m}, soma = {soma_algoritmo(m)})'
          f'({z}, soma = {soma_algoritmo(z)})'
          f'({e}, soma = {soma_algoritmo(e)})'
          f'({t}, soma = {soma_algoritmo(t)})')
    m = m * 2
    z = z * 2
    e = e * 2
    t = t * 2
