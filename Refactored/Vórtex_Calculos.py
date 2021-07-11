def separacao_num(c1):
    u1 = c1 // 1 % 10
    u2 = c1 // 10 % 10
    return u1, u2


def Soma_da_adicao(numero):

    # Variaveis
    n1 = 0
    u1 = 0
    u2 = 0

    cont = 1    # Para conter o loop do while

    if 1 <= numero <= 9:    # Verifica se o numero escolhido é de 1 a 9
        while cont <= 9:    # Enquanto a variavel cont não for 9..
            tab = numero * cont  # recebe a multiplicação
            if tab >= 10:  # Verifica se o resultado é maior que dez
                n1 = tab    # recebe a variavel
                u2 = separacao_num(n1)[0]
                u1 = separacao_num(n1)[1]
                n1 = u1 + u2    # soma as variaveis de captação

            if tab >= 10:  # Se o resultado da soma for maior/igual que 10
                if n1 >= 10:  # se o resultado da soma da multiplicação é maior/igual que 10
                    t1 = separacao_num(n1)[0]
                    t2 = separacao_num(n1)[1]
                    print(f"{numero} X {cont} = {tab} ({u1} + {u2} = {n1}({t2} + {t1} = {t1 + t2}))")
                else:
                    print(f"{numero} X {cont} = {tab} ({u1} + {u2} = {n1})")
            else:
                print(f"{numero} X {cont} = {tab}")
            cont = cont + 1  # soma mais 1 até chegar a sequncia de 9 dentrod o while

    else:
        print("apenas valores de 1 a 9")


def Soma_da_multiplicacao(numero):  # Cria a função e uma entrada

    # Lista com os números de devem ser separados
    lista36 = [3, 6]
    lista9 = [9, 0]

    if numero in lista36:  # Verifica se o número existe dentro da lista
        repeticao = 4   # atribui o número de repetição
    elif numero in lista9:  # Verifica se o número é 9
        repeticao = 3   # atribui o número de repetição
    else:
        repeticao = 8  # atribui o número de repetição

    # Carrinhos que vão levar os números
    t1 = numero
    t2 = numero
    u1 = 0
    u2 = 0

    cont = 3  # variavel responsavel pela continuação do loop

    while cont <= repeticao:  # O loop se encerra a cada ciclo somando +1 um até o valor de repetição
        t3 = t1 + t2  # faz a soma dos numeros
        if t3 >= 10:  # Certifica se o valor de t3 é maior que 10, para o sistema perceber que tem casa decimal
            t4 = t3  # Cria variavel e Copia do valor de t3 para t4, para assim poder somar os digitos
            u1 = t4 // 1 % 10  # Armazena em uma variavel o número da primeira casa
            u2 = t4 // 10 % 10  # Armazena em uma variavel o número da segunda casa
            t3 = u1 + u2  # Coloca o valor da soma das variaveis com cada casa decimal dentro da variavel t3
        if t2 >= 10:
            print(f'{t1} + {t2} = {t3} ({t1} + {t2} = {t1+t2}({u2} + {u1} = {u1+u2}))')  # mostra o resultado'
        else:
            print(f'{t1} + {t2} = {t3} ')  # mostra o resultado'
        t2 = t3  # transforma a variavel no resultado anterior
        t1 = t3  # transforma a variavel no resultado anterior
        cont += 1  # Acresenta +1 para o termino do loop while


numero_menu = ''    # Variavel resposavel pela interação com usuario

while numero_menu != 3:  # Verifica se numero_menu é diferente de 3
    # Pede ao usuario um numero do menu - entrada de dado
    numero_menu = int(input('1 - n * n = n. \n'
                            '2 - n + n = n. \n'
                            '3 - Para finalizar . \n'
                            'Selecione um número do Menu: '))

    if numero_menu == 1:  # Se numero_menu for igual a 1 executa o código
        num = int(input('Insira um número de 1 a 9: '))
        Soma_da_adicao(num)  # chama a função e coloca o dado da entrada

    elif numero_menu == 2:  # Se numero_menu for igual a 1 executa o código
        num = int(input('Selecione um número: '))  # Entrada do número a ser somado
        Soma_da_multiplicacao(num)  # chama a função e coloca o dado da entrada
    else:
        print('Apenas números visiveis no menu')
        if numero_menu != 3:  # Verificação para saber se o usuario vai continuar o código
            condicao = input('Deseja encerar o código? \nresponda com SIM ou NÃO: ')  # entrada de dado do usuario
            if condicao == 'NÃO':  # se (NÃO) ele continua o código
                numero_menu = 0  # o while continua
            elif condicao == 'SIM':  # se (SIM) ele para o código
                break

    print('#====================================================#')
