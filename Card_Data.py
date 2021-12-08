

def load(arq):
    temp = []
    arquivo = open(arq, 'r')
    arquivo.readline()
    for linha in arquivo:
        linha = linha.replace('\n', '')
        linha = linha.replace('"', '')
        dados = linha.split(',')
        dados[2] = int(dados[2])
        dados[4] = int(dados[4])
        dados[9] = int(dados[9])
        dados[10] = int(dados[10])
        dados[11] = int(dados[11])
        dados[12] = int(dados[12])
        dados[13] = float(dados[13])
        dados[14] = int(dados[14])
        dados[15] = float(dados[15])
        dados[16] = float(dados[16])
        dados[17] = int(dados[17])
        dados[18] = int(dados[18])
        dados[19] = float(dados[19])

        # numeros ja convertidos para int ou float
        temp.append(dados)

    arquivo.close()
    return temp


def exibirDados(dados):
    for i in range(len(dados)):
        print(dados[i])


def menu():
    print('Menu')
    print('1 - Carregar dados do arquivo')
    print('2 - Listar todos os dados')
    print('3 - Informar o percentual de pessoas do gênero masculino e feminino que encontram-se na high school')
    print('4 - Criar e mostrar coluna para tempo de relacionamento com o cliente')
    print('5 - Mostrar infos(Quantidade de clientes,Média de tempo de relacionamento,Receita média) para cada cartao')
    print('6 - informar media de limite de credito para clientes com mais de um dependente')
    print('7 - Informar a quantidade de clientes em cada nível educacional')
    print('8 - Gerar um novo arquivo somente com os clientes que possuem mais de 45 anos')
    print('9 - Informar o codigo dos 5 clientes que mais fizeram transacoes nos ultimos 12 meses')
    print('10 - Informar a media de transacao dos clientes de cada tipo de cartao')
    print('11 - Encontrar o cliente mais novo com o maior número de dependentes')
    print('12 - Calcular o numero de clientes casados para cada tipo de cartao ')



def calcular_high_school(main_list):
    contador = 0
    contadorF = 0
    contadorM = 0
    for i in range(len(main_list)):
        if main_list[i][5] == 'High School':
            contador = contador + 1
        if main_list[i][3] == 'F' and main_list[i][5] == 'High School':
            contadorF = contadorF + 1
        if main_list[i][3] == 'M' and main_list[i][5] == 'High School':
            contadorM = contadorM + 1
    print("Clientes no ensino medio: " + str(contador))
    print("Clientes mulheres no ensino medio: " + str(contadorF))
    print("Clientes homens no ensino medio: " + str(contadorM))
    percentual_m = (100*contadorM)/contador
    percentual_f = (100 * contadorF) / contador
    print("O percentual de mulheres no ensino medio: " + str(percentual_f) + "%")
    print("O percentual de homens no ensino medio: " + str(percentual_m) +"%")


def tempo_cliente(lista_principal):
    maior = 0
    # maior guarda o valor do cliente mais antigo
    #as classificacoes de tempo é igual a o tempo do cliente mais antigo dividido por 3
    for i in range(1,len(lista_principal)):
        #está lendo o titulo da coluna? assim ele pula a primeira linha
        testando = lista_principal[i][9]
        if testando > maior:
            maior = lista_principal[i][9]
    matriz_nova = criar_classificacao(matriz)
    print(matriz_nova)
    print("O cliente mais antigo tem " + str(maior) + " meses de tempo de relacionamento.")

def criar_classificacao(matrix):
    # 0-18 relacionamento curto
    # 19-37 relacionamento medio
    # 38-56 relacionamento longo
    # criar coluna com essa classificacao para os clientes
    for i in range(len(matrix)):
        categoria = ''
        if matrix[i][9] < 19:
            categoria = 'relacionamento curto'
        elif matrix[i][9] >= 19 and matrix[i][9] < 38:
            categoria = 'relacionamento medio'
        else:
            categoria = 'relacionamento longo'
        matrix[i].append(categoria)
    return matrix

def card_types_info(matriz1):
    card_blue = {}
    card_silver = {}
    card_gold = {}
    card_platinum = {}
    contador_blue = 0
    contador_silver = 0
    contador_gold = 0
    contador_platinum = 0
    soma_blue = 0
    soma_silver = 0
    soma_gold = 0
    soma_platinum = 0
    # renda media calculada com Total_Trans_Amt matriz1[i][17]
    renda_blue = 0
    renda_silver = 0
    renda_gold = 0
    renda_platinum = 0

    for i in range(len(matriz1)):
        if matriz1[i][8] == 'Blue':
            contador_blue = contador_blue + 1
            soma_blue = matriz1[i][9] + soma_blue
            renda_blue = matriz1[i][17] + renda_blue


        if matriz1[i][8] == 'Silver':
            contador_silver = contador_silver + 1
            soma_silver = matriz1[i][9] + soma_silver
            renda_silver = matriz1[i][17] + renda_silver

        if matriz1[i][8] == 'Gold':
            contador_gold = contador_gold + 1
            soma_gold = matriz1[i][9] + soma_gold
            renda_gold = matriz1[i][17] + renda_gold

        if matriz1[i][8] == 'Platinum':
            contador_platinum = contador_platinum + 1
            soma_platinum = matriz1[i][9] + soma_platinum
            renda_platinum = matriz1[i][17] + renda_platinum

    media_tempo_blue = soma_blue/contador_blue
    media_tempo_silver = soma_silver/contador_silver
    media_tempo_gold = soma_gold/contador_gold
    media_tempo_platinum = soma_platinum/contador_platinum

    media_renda_blue = renda_blue/contador_blue
    media_renda_silver = renda_silver / contador_silver
    media_renda_gold = renda_gold / contador_gold
    media_renda_platinum = renda_platinum / contador_platinum


    print("Tipo de cartao: numero de clientes,media de relacionamento, renda media.")
    card_blue["Blue"] = contador_blue,media_tempo_blue,media_renda_blue
    card_silver["Silver"] = contador_silver,media_tempo_silver,media_renda_silver
    card_gold["Gold"] = contador_gold,media_tempo_gold,media_renda_gold
    card_platinum["Platinum"] = contador_platinum,media_tempo_platinum,media_renda_platinum
    print(card_blue)
    print(card_silver)
    print(card_gold)
    print(card_platinum)


def media_limite_dependentes(matriz3):
    soma_credito = 0
    contador = 0
    for i in range(len(matriz3)):
        if matriz3[i][4] > 1:
            contador = contador + 1
            soma_credito = matriz3[i][13] + soma_credito

    media_credito = soma_credito/contador
    return media_credito

def nmr_nivel_educacional(matriz4):
    contador_unknown = 0
    contador_uneducated = 0
    contador_high_school = 0
    contador_college = 0
    contador_graduate = 0
    contador_doctorate = 0
    contador_pos = 0
    for i in range(len(matriz4)):
        if matriz4[i][5] == 'Unknown':
            contador_unknown = contador_unknown + 1

        if matriz4[i][5] == 'Uneducated':
            contador_uneducated = contador_uneducated + 1

        if matriz4[i][5] == 'High School':
            contador_high_school = contador_high_school + 1

        if matriz4[i][5] == 'College':
            contador_college = contador_college + 1

        if matriz4[i][5] == 'Graduate':
            contador_graduate = contador_graduate + 1

        if matriz4[i][5] == 'Doctorate':
            contador_doctorate = contador_doctorate + 1

        if matriz4[i][5] == 'Post-Graduate':
            contador_pos = contador_pos + 1
    print("Niveis educacionais:")
    print("Desconhecido: " + str(contador_unknown))
    print("Sem estudo: " + str(contador_uneducated))
    print("Ensino medio: " + str(contador_high_school))
    print("Faculdade em andamento: " + str(contador_college))
    print("Graduado: " + str(contador_graduate))
    print("Pós Graduado: " + str(contador_pos))
    print("Doutorado: " + str(contador_doctorate))

def transacoes_12meses(matriz5):
    dic = {}
    maior1 = 0
    maior2 = 0
    maior3 = 0
    maior4 = 0
    maior5 = 0
    n_m1 = 0
    n_m2 = 0
    n_m3 = 0
    n_m4 = 0
    n_m5 = 0

    for i in range(len(matriz5)):
        #Total_Trans_Ct a coluna de interesse
        if matriz5[i][18] > maior1 and matriz5[i][18] >= maior2 and matriz5[i][18] >= maior3 and matriz5[i][18] >= maior4 and matriz5[i][18] >= maior5:
            maior1 = matriz5[i][18]
            n_m1 = matriz5[i][0]

        elif matriz5[i][18] > maior2 and matriz5[i][18] <= maior1  and matriz5[i][18] >= maior3 and matriz5[i][18] >= maior4 and matriz5[i][18] >= maior5:
            maior2 = matriz5[i][18]
            n_m2 = matriz5[i][0]

        elif matriz5[i][18] > maior3 and matriz5[i][18] <= maior1 and matriz5[i][18] <= maior2  and matriz5[i][18] >= maior4 and matriz5[i][18] >= maior5:
            maior3 = matriz5[i][18]
            n_m3 = matriz5[i][0]

        elif matriz5[i][18] > maior4 and matriz5[i][18] <= maior1 and matriz5[i][18] <= maior2 and matriz5[i][18] <= maior3 and matriz5[i][18] >= maior5:
            maior4 = matriz5[i][18]
            n_m4 = matriz5[i][0]

        elif matriz5[i][18] > maior5 and matriz5[i][18] <= maior1 and matriz5[i][18] <= maior2 and matriz5[i][18] <= maior3 and matriz5[i][18] <= maior4:
            maior5 = matriz5[i][18]
            n_m5 = matriz5[i][0]

    dic["cliente1"] = maior1, n_m1
    dic["cliente2"] = maior2, n_m2
    dic["cliente3"] = maior3, n_m3
    dic["cliente4"] = maior4, n_m4
    dic["cliente5"] = maior5, n_m5
    return dic

def media_transacoes_card(matriz6):
    soma_tran_blue = 0
    soma_tran_silver = 0
    soma_tran_gold = 0
    soma_tran_platinum = 0
    cont_blue = 0
    cont_silver = 0
    cont_gold = 0
    cont_platinum = 0

    for i in range(len(matriz6)):
        if matriz6[i][8] == 'Blue':
            cont_blue = cont_blue + 1
            soma_tran_blue = matriz6[i][18] + soma_tran_blue

        if matriz6[i][8] == 'Silver':
            cont_silver = cont_silver + 1
            soma_tran_silver = matriz6[i][18] + soma_tran_silver

        if matriz6[i][8] == 'Gold':
            cont_gold = cont_gold + 1
            soma_tran_gold = matriz6[i][18] + soma_tran_gold

        if matriz6[i][8] == 'Platinum':
            cont_platinum = cont_platinum + 1
            soma_tran_platinum = matriz6[i][18] + soma_tran_platinum

    media_trans_blue = soma_tran_blue/cont_blue
    media_trans_silver = soma_tran_silver/cont_silver
    media_trans_gold = soma_tran_gold/cont_gold
    media_trans_platinum = soma_tran_platinum/cont_platinum

    print("A media de transacoes para o cartao blue: " + str(media_trans_blue))
    print("A media de transacoes para o cartao silver: " + str(media_trans_silver))
    print("A media de transacoes para o cartao gold: " + str(media_trans_gold))
    print("A media de transacoes para o cartao platinum: " + str(media_trans_platinum))


def mais_novo_maior_dependentes(matriz7):
    mais_novo = 1000
    maior_dependentes = 0
    for i in range(len(matriz7)):
        if matriz7[i][4] > maior_dependentes and matriz7[i][2] < mais_novo:
            mais_novo = matriz7[i][2]
            maior_dependentes = matriz7[i][4]

    print("A idade do cliente mais novo com o maior numero de dependentes é: " + str(mais_novo))
    print("Esse cliente tem "+ str(maior_dependentes) + " dependentes")

def casados_card(matriz8):
    contador_blue = 0
    contador_silver = 0
    contador_gold = 0
    contador_platinum = 0

    for i in range(len(matriz8)):
        if matriz8[i][8] == 'Blue' and matriz8[i][6] == 'Married':
            contador_blue = contador_blue + 1

        if matriz8[i][8] == 'Silver' and matriz8[i][6] == 'Married':
            contador_silver = contador_silver + 1

        if matriz8[i][8] == 'Gold' and matriz8[i][6] == 'Married':
            contador_gold = contador_gold + 1

        if matriz8[i][8] == 'Platinum' and matriz8[i][6] == 'Married':
            contador_platinum = contador_platinum + 1
    print("O numero de pessoas casadas com cada tipo de cartao é:")
    print("Blue: " + str(contador_blue))
    print("Silver: " + str(contador_silver))
    print("Gold: " + str(contador_gold))
    print("Platinum: " + str(contador_platinum))


def criar_arquivo_45age(matriz9, arquivs):

        arquivo_temp = open(arquivs,'w')

        for j in range(len(matriz9)):
            if matriz9[j][2] > 45:
                linha = str(matriz9[j][0]) + ',' + str(matriz9[j][2]) + ',' + str(matriz9[j][3]) + ',' + str(matriz9[j][13]) + '\n'
                arquivo_temp.write(linha)

        arquivo_temp.close()

arquivo_new = 'dados_clientes45.txt'
matriz = []
opcao = -1
while opcao != 0:
    menu()
    opcao = int(input('Digite a opcao: '))
    if opcao == 1:
     nome_arq = 'BankChurners.csv'
     #diretorio temporário, é necessario colocar os arquivos em uma mesma pasta posteriormente
     matriz = load(nome_arq)

    elif opcao == 2:
        exibicao = exibirDados(matriz)
        print(exibicao)

    elif opcao == 3:
        calcular_high_school(matriz)

    elif opcao == 4:
        tempo_cliente(matriz)

    elif opcao == 5:
        card_types_info(matriz)

    elif opcao == 6:
        media_cred = media_limite_dependentes(matriz)
        print("A média de limite de credito para clientes com mais de um dependente: " + str(media_cred))

    elif opcao == 7:
        nmr_nivel_educacional(matriz)

    elif opcao == 8:
        criar_arquivo_45age(matriz,arquivo_new)

    elif opcao == 9:
        transacoes_nmro = transacoes_12meses(matriz)
        print(transacoes_nmro)

    elif opcao == 10:
        media_trans_card = media_transacoes_card(matriz)

    elif opcao == 11:
        novo_dependentes = mais_novo_maior_dependentes(matriz)

    elif opcao == 12:
        casados_cards = casados_card(matriz)