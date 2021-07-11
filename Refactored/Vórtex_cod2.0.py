def funcao_vortex(numero):
    t1 = numero
    t2 = numero + 1

    continua = 3
    while continua == 8:
        t3 = t1 + t2
        if t3 >= 10:  # Se t3 for maior que 10 elimina as casas decimais
            t4 = t3
            u1 = t4 // 1 % 10
            u2 = t4 // 10 % 10
            t3 = u1 + u2
            print(t3)

        continua += 1


num = int(input('Selecione um numero: '))
funcao_vortex(num)
