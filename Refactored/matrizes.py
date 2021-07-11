# matriz = []
# for i in range(n):
#     matriz.append([0]*m)
# for i in range(n):
#     print(matriz[i])

# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for l in range(0, 3):
#     for c in range(0, 3):
#         matriz[l][c] = int(input(f'Digite um valor para [{l}],[{c}]: '))
#
# # Mostrar estrutura na tela
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{matriz[l][c]:^5}]', end='')  # (:^5) centraliza os valores
#     print()

# Modificada de 1, 9
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
cont = 0
while cont != 9:
    for l in range(0, 3):
        for c in range(0, 3):
            cont += 1
            matriz[l][c] = cont
        # matriz[l][c] = int(input(f'Digite um valor para [{l}],[{c}]: '))

# Mostrar estrutura na tela
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')  # (:^5) centraliza os valores
    print()