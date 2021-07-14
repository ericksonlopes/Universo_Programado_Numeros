import random

# 1k a 10k
numeros = range(0, 10000)

# Escolher n números da lista
escolhidos = random.sample(numeros, 20)

# # Exibir numeros escolhidos
# print(escolhidos)

num_string = []
extract = [[num_string.append(s) for s in str(t)] for t in escolhidos]
num_string.sort()
uniques = sorted(set(num_string))
len_num = len(num_string)

print("Total:", len_num)

for unique in uniques:
    print(f"{unique}│{num_string.count(unique):>3}│ {(num_string.count(unique) / len_num) * 100:.3}%")

