# sequencia = int(input('Digite até onde quer ver a sequência de divisores: '))
sequencia = 15
divisores = []

for num in range(2, sequencia + 1):
    for numero in range(1, int(num / 2 + 1)):
        if num % numero == 0:
            divisores.append(numero)
    print(num, divisores)
    divisores.clear()

divi = 13
print([num for num in range(1, divi + 1) if divi % num == 0])

