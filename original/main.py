from dataclasses import dataclass

@dataclass
class Jogador:
    nome: str
    num: int


# Cria uma lista de listas preencida com o valor
def crieMatriz(tam, valor):
    matriz = [] # lista vazia
    for i in range(tam):
        # cria a linha i
        linha = [] # lista vazia
        for j in range(tam):
            linha.append(valor)

        # coloque linha na matriz
        matriz.append(linha)

    return matriz

def printMatriz(matriz):
    print()
    linha = "-" * ((len(matriz) * 4) - 1)
    for i in range(len(matriz) - 1):
        print("", end=" ")
        print(*matriz[i], sep = " | ")
        print(linha)

    print("", end=" ")
    print(*matriz[-1], sep = " | ")
    print("\n")

def checa_horizontal(tabuleiro, linha, coluna)-> int:
    tam_mat = len(tabuleiro)
    count = 0
    vencedor = -1
    for i in range (tam_mat):
        for j in range (tam_mat):
            if(tabuleiro[i][j] == tabuleiro[linha][coluna]):
                count = count + 1
            else:
                count = 0
            if(count > 2):
                vencedor = tabuleiro[linha][coluna]
                return vencedor 
        count = 0
    
    return vencedor


def checa_vertical(tabuleiro, linha, coluna)-> int:
    tam_mat = len(tabuleiro)
    count = 0
    vencedor = -1
    for j in range (tam_mat):
        for i in range (tam_mat):
            if(tabuleiro[i][j] == tabuleiro[linha][coluna]):
                count = count + 1
            else:
                count = 0
            if(count > 2):
                vencedor = tabuleiro[linha][coluna]
                return vencedor
        count = 0
    
    return vencedor


def checa_diagonal(tabuleiro, linha, coluna)-> int:
    tam_mat = len(tabuleiro)
    count = 0
    vencedor = -1
    for d in range (tam_mat):
        for j in range (tam_mat):
            if(j + d >= tam_mat):
                break
            if(tabuleiro[j][j+d] == tabuleiro[linha][coluna]):
                count = count + 1
            else:
                count = 0
            if(count > 2):
                vencedor = tabuleiro[linha][coluna]
                return vencedor
        count = 0

    count = 0
    for d in range (tam_mat):
        for j in range (tam_mat):
            if(j + d >= tam_mat):
                break
            if(tabuleiro[j+d][j] == tabuleiro[linha][coluna]):
                count = count + 1
            else:
                count = 0
            if(count > 2):
                vencedor = tabuleiro[linha][coluna]
                return vencedor
        count = 0

    count = 0
    for d in range (tam_mat):
        for j in range (tam_mat):
            if(tam_mat - 1 - d - j < 0):
                break
            if(tabuleiro[j][tam_mat - 1 - d - j] == tabuleiro[linha][coluna]):
                count = count + 1
            else:
                count = 0
            if(count > 2):
                vencedor = tabuleiro[linha][coluna]
                return vencedor
        count = 0

    count = 0
    for d in range (tam_mat):
        for j in range (tam_mat):
            if(j + d >= tam_mat):
                break
            if(tabuleiro[tam_mat - j - 1][j + d] == tabuleiro[linha][coluna]):
                count = count + 1
            else:
                count = 0
            if(count > 2):
                vencedor = tabuleiro[linha][coluna]
                return vencedor
        count = 0
    
    return vencedor

def verificaVencedor(tabuleiro, linha, coluna) -> int:
    ret = -1

    ret = checa_diagonal(tabuleiro, linha,coluna)
    if ret != -1:
        return ret

    ret = checa_vertical(tabuleiro, linha,coluna) 
    if ret != -1:
        return ret

    ret = checa_horizontal(tabuleiro, linha,coluna)
    
    return ret

def main():
    print("\n      xoxoxoxo JOGO DA VELHA xoxoxox\n\n")
    tam_matriz = int(input("Entre com o tamanho do tabuleiro: "))
    while tam_matriz > 10 or tam_matriz < 3:
        tam_matriz = int(input("\nTamanho inválido. Entre novamente com o tamanho: "))

    matriz = crieMatriz(tam_matriz, " ")
    qnt_jogadores = int(input("\nEntre com a quantidade de jogadores: "))
    while qnt_jogadores > 5 or qnt_jogadores < 2:
        qnt_jogadores = int(input("\nQuantidade inválida. Entre novamente com o número de jogadores: "))
        

    vetor_jogadores = []
    for i in range(qnt_jogadores):
        aux = str(input("\nEntre com o nome do jogador {}: ".format(i+1)))
        temp = Jogador(aux, i+1)
        vetor_jogadores.append(temp)

    nome_arq = str(input("\nEntre com o nome do arquivo a qual deseja salvar os dados: "))
    arquivo = open(nome_arq, 'w')
    arquivo.write('Tamanho do tabuleiro = ' + str(tam_matriz) + '\n')
    arquivo.write('Quantidade de Jogadores = ' + str(qnt_jogadores) + '\n')
    for i in range(len(vetor_jogadores)):
        arquivo.write('Jogador ' + str(i+1) + ' = ' + vetor_jogadores[i].nome + '\n')
    print('\nEntre com as jogadas (id, linha, coluna)')
    arquivo.write('Jogadas (id, linha, coluna):' + '\n')

    jogadas = 1
    vencedor = -1
    while jogadas <= (len(matriz) ** 2):
        id_jogador, linha, coluna = input('Jogada ' + str(jogadas) + ': ').split()
        linha = int(linha)
        coluna = int(coluna)
        while (linha >= tam_matriz or coluna >= tam_matriz) or matriz[linha][coluna] != " ":
            print('\nJogada errada. Tente novamente')
            id_jogador, linha, coluna = input('jogada ' + str(jogadas) + ': ').split()
            linha = int(linha)
            coluna = int(coluna)

        arquivo.write('Jogada ' + str(jogadas) + ': id=' + str(id_jogador) + ", linha=" + str(linha) + ", coluna=" + str(coluna) + '\n')
        matriz[linha][coluna] = id_jogador
        vencedor =int(verificaVencedor(matriz, linha, coluna)) 
        if vencedor != -1:
            vencedor -= 1
            printMatriz(matriz)
            break
        printMatriz(matriz)
        jogadas += 1

    if jogadas == ((len(matriz) ** 2) + 1):
        print('Deu velha! =(')
        arquivo.write('Deu velha! =(\n')
    else:
        print('Vencedor: ' + vetor_jogadores[int(vencedor)].nome)
        arquivo.write('Vencedor: ' + vetor_jogadores[int(vencedor)].nome + '\n')

    arquivo.close()

if __name__ == "__main__":
    main()
