dimensao = 0
n_jogadores = 0
ID_jogada = ""
linha_jogada = -1
coluna_jogada = -1
nome_jogadores = []
id_jogadores = []
tabuleiro = None
arquivo_partida = None
arquivo_leitura = None
conteudo_arquivo = None
contador_jogadas = 0
modo_jogo = 0 #0 para tela, 1 para arquivo


def checa_horizontal():
    count = 0
    for i in range (dimensao):
        for j in range (dimensao):
            if(tabuleiro[i][j] == ID_jogada):
                count = count + 1
            else:
                count = 0
            if(count > 2):
                return True
        count = 0
    return False


def checa_vertical():
    count = 0
    for j in range (dimensao):
        for i in range (dimensao):
            if(tabuleiro[i][j] == ID_jogada):
                count = count + 1
            else:
                count = 0
            if(count > 2):
                return True
        count = 0
    return False


def checa_diagonal():
    count = 0
    for d in range (dimensao):
        for j in range (dimensao):
            if(j + d >= dimensao):
                break
            if(tabuleiro[j][j+d] == ID_jogada):
                count = count + 1
            else:
                count = 0
            if(count > 2):
                return True
        count = 0

    count = 0
    for d in range (dimensao):
        for j in range (dimensao):
            if(j + d >= dimensao):
                break
            if(tabuleiro[j+d][j] == ID_jogada):
                count = count + 1
            else:
                count = 0
            if(count > 2):
                return True
        count = 0

    count = 0
    for d in range (dimensao):
        for j in range (dimensao):
            if(dimensao - 1 - d - j < 0):
                break
            if(tabuleiro[j][dimensao - 1 - d - j] == ID_jogada):
                count = count + 1
            else:
                count = 0
            if(count > 2):
                return True
        count = 0

    count = 0
    for d in range (dimensao):
        for j in range (dimensao):
            if(j + d >= dimensao):
                break
            if(tabuleiro[dimensao - j - 1][j + d] == ID_jogada):
                count = count + 1
            else:
                count = 0
            if(count > 2):
                return True
        count = 0
    return False


def cria_matriz(n_linhas, n_colunas, valor):
    matriz = []
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            linha += [valor]
            
        matriz += [linha]
    
    return matriz


def imprime_matriz(m):
    for x in m:
        print(x)


def inicia_arquivo_registro():
    global arquivo_partida
    arquivo_partida= open(input("insira o nome do aquivo: "), "w")


def ler_dimensao_e_jogadores():
    global dimensao
    global n_jogadores
    while (dimensao < 3 or dimensao > 10 or n_jogadores < 2 or n_jogadores > 5):
        if(modo_jogo == 0):
            entrada = input("Insira a Dimensao e o numero de jogadores: ")
            entrada = entrada.split(" ")
            dimensao = int(entrada[0])
            n_jogadores = int(entrada[1])
            if(dimensao == 1 and n_jogadores == 0):
                define_modo_jogo(1)            
        else:
            dimensao = int(conteudo_arquivo[0].split(" ")[0]) #Linha 0 do arquivo, primeiro dado
            n_jogadores = int(conteudo_arquivo[0].split(" ")[1])  # Linha 0 do arquivo, segundo dado


def define_modo_jogo(modo):
    global dimensao
    global n_jogadores
    global conteudo_arquivo
    global arquivo_leitura
    global modo_jogo

    modo_jogo = modo #Modo Arquivo
    dimensao = 0
    n_jogadores = 0
    if(modo == 1):
        arquivo_leitura = open(input("insira o nome do arquivo de jogadas: "), "r")
        conteudo_arquivo = []
        for linha in arquivo_leitura:
            conteudo_arquivo.append(linha)
        arquivo_leitura.close()    
    

def ler_nomes_jogadores():
    global nome_jogadores
    global id_jogadores
    if(modo_jogo == 0):
        print("Insira os nomes dos jogares seguidos de seus IDs:")
        for x in range (n_jogadores):
            entrada = input()
            entrada = entrada.split(" ")
            nome_jogadores.append(entrada[0])
            id_jogadores.append(int(entrada[1]))
    else:
        for i in range (1, n_jogadores + 1):
            entrada = conteudo_arquivo[i]
            entrada = entrada.split(" ")
            nome_jogadores.append(entrada[0])
            id_jogadores.append(int(entrada[1]))  


def registra_dimensao_e_jogadores():
    arquivo_partida.write("Dimensao do Tabuleiro: " + str(dimensao) + "\n")
    arquivo_partida.write("Numero de Jogadores: " + str(n_jogadores) + "\n\nJogadores: \n")
    for i in range (n_jogadores):
        arquivo_partida.write(nome_jogadores[i] + " " + str(id_jogadores[i]) + "\n")
    arquivo_partida.write("\nJogadas: ")


def inicia_jogo():   
    inicia_arquivo_registro()   
    ler_dimensao_e_jogadores()
    ler_nomes_jogadores()
    registra_dimensao_e_jogadores()    
    

def ler_jogada():  
    global linha_jogada
    global coluna_jogada
    global ID_jogada
    global contador_jogadas

    if(modo_jogo == 0):
        entrada = input("Insira a proxima jogada: \n")
    elif(1 + n_jogadores + contador_jogadas <= len(conteudo_arquivo)):
        entrada = conteudo_arquivo[1 + n_jogadores + contador_jogadas].strip()

        print(entrada)
        contador_jogadas = contador_jogadas + 1        
    else:
        print("Arquivo de jogadas Invalido")

    entrada = entrada.split(" ")
    ID_jogada = int(entrada[0])
    linha_jogada = int(entrada[1])
    coluna_jogada = int(entrada[2])
    if(linha_jogada >= dimensao or coluna_jogada >= dimensao or linha_jogada < 0 or coluna_jogada < 0):
        entrada = input("Jogada Invalida\nInsira novamente a proxima jogada: \n")       
        ler_jogada()


def cheio():
    for i in range (dimensao):
        for j in range (dimensao):
            if(tabuleiro[i][j] == 0):
                return False
    return True


def checa_tabuleiro():
    global ID_jogada
    if(cheio()):
        ID_jogada = -1
        return True
    return checa_horizontal() or checa_vertical() or checa_diagonal()


def joga_no_tabuleiro():
    if(ID_jogada in id_jogadores and linha_jogada < dimensao and coluna_jogada < dimensao and linha_jogada >= 0 and coluna_jogada >= 0 and tabuleiro[linha_jogada][coluna_jogada] == 0):
        tabuleiro[linha_jogada][coluna_jogada] = ID_jogada
        arquivo_partida.write(str(ID_jogada) + " " + str(linha_jogada) + " " + str(coluna_jogada) + "\n")


def jogar():
    fim_de_jogo = False
    while (not fim_de_jogo):
        ler_jogada()
        joga_no_tabuleiro()
        imprime_matriz(tabuleiro)
        fim_de_jogo = checa_tabuleiro()
    if(ID_jogada == -1):
        print("Sem Vencedor")
        arquivo_partida.write("Sem Vencedor\n")
    else:
        for i in range (n_jogadores):
            if(id_jogadores[i] == ID_jogada):
                print(nome_jogadores[i] + " Ganhou o Jogo")
                arquivo_partida.write(nome_jogadores[i] + " Ganhou o Jogo\n")


inicia_jogo()
tabuleiro = cria_matriz(dimensao,dimensao, 0)
jogar()
arquivo_partida.close()