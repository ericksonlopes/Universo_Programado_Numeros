def fatorial(n):
    c = n
    f = 1
    print(f'Calculando {c}! = ', end='')
    while c > 0:
        print(f'{c}', end='')
        print(' x ' if c > 1 else ' = ', end='')
        # f = f * c
        f *= c
        c -= 1
    print(f)


n_fatorial = int(input("Digite um núemero para calcular seu fatorial: "))
fatorial(n_fatorial)
