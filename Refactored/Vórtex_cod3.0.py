def funcao_vortex(numero):
    n = numero
    cont = 1

    if 1 <= n <= 10:
        while cont <= 10:
            tab = n * cont
            print(f"{n} X {cont} = {tab}")
            cont = cont + 1

    else:
        print("apenas valores de 1 a 10")


num = int(input('Insira um número de 1 a 10: '))
funcao_vortex(num)

