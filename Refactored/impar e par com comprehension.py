"""
Primos com list comprehension
"""
par = [numero for numero in range(0, 10, 2)]
print(par)

par = [numero for numero in range(10) if numero % 2 == 0]
print(par)

impar = [numero for numero in range(1, 10, 2)]
print(impar)

impar = [numero for numero in range(10) if not numero % 2 == 0]
print(impar)
