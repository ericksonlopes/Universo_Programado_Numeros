def funcao_vortex(numero):
    t1 = numero
    t2 = numero + 1

    continua = 3
    u1 = 0
    u2 = 0

    while continua <= 8:
        t3 = t2 + t1

        if t3 >= 10:  # Se t3 for maior que 10 elimina as casas decimais
            t4 = t3
            u1 = t4 // 1 % 10
            u2 = t4 // 10 % 10
            t3 = u1 + u2

        if t1 + t2 >= 10:   # Se a soma de  t1 + t2 for maior que 10
            print(f'{t1} + {t2} = {t3} ({t1} + {t2} = {t1 + t2} ({u2} + {u1} = {u2 + u1}))')
        else:  # caso não seja ele imprimira sem adições de string
            print(f'{t1} + {t2} = {t3}')

        t1 = t3
        t2 = t3 + 1

        continua += 1


num = 1
funcao_vortex(num)
