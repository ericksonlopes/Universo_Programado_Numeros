from math import *

def soma_algarismo(numero):
    while not numero < 10:
        numero = sum(list(map(lambda x: int(x), [num for num in str(numero)])))
    return numero


for num in range(0, 500):
    if len(str(sqrt(num))) < 5:
        print(f'{soma_algarismo(num):^4}   {num:^4}   {sqrt(num):^4}')

