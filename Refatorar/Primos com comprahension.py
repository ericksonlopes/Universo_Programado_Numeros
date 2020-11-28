num = int(input('Digite para ver seus divisores: '))

lista = [numero for numero in range(1, num + 1) if num % numero == 0]

print('primo' if len(lista) <= 2 else 'não primo')

