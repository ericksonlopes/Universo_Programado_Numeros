# Matrizes 3x3

matriz = [0, 0, 0], [0, 0, 0], [0, 0, 0]  # Matriz
spar = mai = scol = 0  # Soma dos pares/ maior valor / soma das colunas = 0

# Adicionando os dados da matriz
for l in range(0, 3):  # laço para todas as linhas
    for c in range(0, 3):  # laço para todas as colunas
        # Armazenamento dos dados do laço
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

# Imprime o laço a cada 3 colunas preenchidas pulando uma linha
print('-=' * 15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')  # Imprime os 3 valores e pula uma linha
        if matriz[l][c] % 2 == 0:  # Se o valor da matriz for divisivel por 2 com resto 0
            spar += matriz[l][c]  # Add o valor na lista spar
    print()

print('-=' * 15)
print(f'A soma dos valores pares é {spar}.')

# Como a coluna é fixa e a linha que variará, mantemos o [2] e solicitamos o valor de [l]
for l in range(0, 3):
    scol += matriz[l][2]  # Soma dos numeros das linhas da coluna 2
print(f'A soma dos valores da terceira coluna é {scol}.')

#       COLUNA COLUNA  COLUNA
#          0      1      2
# LINHA 0
# LINHA 1   X      X      X
# LINHA 2

# LINHA - COLUNA
#  1        0
#  1        1
#  1        2
for c in range(0, 3):
    if c == 0:  # Se a minha coluna for igual a 0.
        mai = matriz[1][c]  # A lista mai será a posição 1 na coluna [c]
    elif matriz[1][c] > mai:  # Se o valor da posição 1 na coluna[c] for maior que a lista mai
        mai = matriz[1][c]  # Então a lista mai será o valor da posição 1 da coluna [c]

print(f'O mair valor da segunda linha é {mai}.')
