from math import sqrt


def soma_algarismo(dado_recebido):
    def soma_alga(dado):
        lista_numeros = list(map(lambda trans_num: int(trans_num),
                                 filter(lambda retira_num: retira_num.isnumeric(), str(dado))))
        return sum(lista_numeros)

    final = soma_alga(dado_recebido)
    while final >= 10:
        final = soma_alga(str(final))
    return final


print("[Soma][Num] [Raiz]")
[print(f'{soma_algarismo(num):^5}', f"{'√' + str(num):^5}", f"{sqrt(num):^5}") for num in range(1, 2000) if
 sqrt(num) == int(sqrt(num))]

