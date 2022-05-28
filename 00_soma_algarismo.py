def soma_algarismo(dado_recebido):

    def soma_alga(dado):
        lista_numeros = list(map(lambda trans_num: int(trans_num),
                                 filter(lambda retira_num: retira_num.isnumeric(), str(dado))))
        return sum(lista_numeros)

    final = soma_alga(dado_recebido)
    while final >= 10:
        final = soma_alga(str(final))
    return final


# estudar nova formula
data = '1  , 1,  ,1, 54 jh,j 1 , 1'

number = sum(int(_) for _ in data if _.isnumeric())

while number >= 10:
    number = sum(int(_) for _ in str(number) if _.isnumeric())

print(number)

print(soma_algarismo('1///--aksjbfsf1'))

print(soma_algarismo(45))

print(soma_algarismo("2+3"))

print(f'5 * 7 = {5 * 7}, soma das casas -> {soma_algarismo(5 * 7)}')
