def soma_algarismo(dado_recebido):
    def soma_alga(dado):
        lista_numeros = list(map(lambda trans_num: int(trans_num),
                                 filter(lambda retira_num: retira_num.isnumeric(), str(dado))))
        return sum(lista_numeros)

    final = soma_alga(dado_recebido)
    while final >= 10:
        final = soma_alga(str(final))
    return final


circ = 360
print(f'[{"X / 2":^20}]', '[ Soma casas ]')
for item in range(22):
    print(f'{circ:>20}', f'{soma_algarismo(circ):>9}')
    circ = circ / 2
