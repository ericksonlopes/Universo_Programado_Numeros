# algarismo para Saida dos primos e nao primos
def maior_primo(num):
    primo = []
    tot = 0
    for c in range(1, num + 1):  # loop para sequancia de 1 até o numero escolhido
        if num % c == 0:    # se o resto da vidisao entre numero e o numero atual do (c) for igual a zero
            print('\033[33m')  # muda a cor da linha
            primo.append(c)  # coloca dentro da lista os números divisiveis
            tot += 1
        else:  # se caso nao seja primo
            print('\033[31m')

        print('{} '.format(c), primo, end='')  # Imprime tudo, com if muda a cor da mesma linha

    if tot == 2:  # Verifica se o numero é primo
        print(f'\n{num} é PRIMO!')
    else:
        print(f'\n {num} NÃO É PRIMO!')

    return f'\n\033[mO número {num} é divisivel {tot} vezes'  # Imprime o maior número primo dentro da sequencia


n = int(input('Digite um número: '))
print(maior_primo(n))

# Código apenas para saída dos números primos
# def maior_primo(num):
#     primo = []
#     tot = 0
#     for c in range(1, num + 1):  # loop para sequancia de 1 até o numero escolhido
#         if num % c == 0:    # se o resto da vidisao entre numero e o numero atual do (c) for igual a zero
#             print('\033[33m')  # muda a cor da linha
#             primo.append(c)  # coloca dentro da lista os números divisiveis
#             print('{}'.format(c), primo, end='')
#             tot += 1
#         # else:  # se caso nao seja primo
#         #     print('\033[31m')
#
#         # print('{} '.format(c), primo, end='')  # Imprime tudo, com if muda a cor da mesma linha
#
#     return f'\nO número {num} é divisivel {tot} vezes'  # Imprime o maior número primo dentro da sequencia
#
#
# n = int(input('Digite um número: '))
# print(maior_primo(n))
