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

def verificaVencedor(tabuleiro, linha, coluna) -> int:
    tam_mat = len(tabuleiro)
    vencedor = -1
    count = 0
    for i in range(-1, 1, 1):
        if coluna+i >= 0 and coluna+i < tam_mat and linha-1 >= 0 and tabuleiro[linha-1][coluna+i] == tabuleiro[linha][coluna]:
            count += 1
            if coluna+(2 * i) >= 0 and coluna+(2 * i) < tam_mat and linha-2 >= 0 and tabuleiro[linha-2][coluna+(2 * i)] == tabuleiro[linha][coluna]:
                vencedor = tabuleiro[linha][coluna]
                break;
        if coluna+i >= 0 and coluna+i < tam_mat and linha+1 < tam_mat and tabuleiro[linha+1][coluna+i] == tabuleiro[linha][coluna]:
            count += 1
            if coluna+(2 * i) >= 0 and coluna+(2 * i) < tam_mat and linha+2 < tam_mat and tabuleiro[linha+2][coluna+(2 * i)] == tabuleiro[linha][coluna]:
                vencedor = tabuleiro[linha][coluna]
                break;
            if count == 1 and linha+1 < tam_mat and coluna + (i * -1) < tam_mat and coluna + (i * -1) >= 0 and tabuleiro[linha][coluna] == tabuleiro[linha+1][coluna + (i * -1)]:
                vencedor = tabuleiro[linha][coluna]
                break;
        if count == 2:
            vencedor = tabuleiro[linha][coluna]
            break;
        count = 0

    count = 0


    if coluna-1 >= 0 and tabuleiro[linha][coluna] == tabuleiro[linha][coluna - 1]:
        count += 1
        if coluna-2 >= 0 and tabuleiro[linha][coluna] == tabuleiro[linha][coluna - 2]:
            vencedor = tabuleiro[linha][coluna]
    if coluna+1 < tam_mat and tabuleiro[linha][coluna] == tabuleiro[linha][coluna + 1]:
        count += 1
        if coluna+2 < tam_mat and tabuleiro[linha][coluna] == tabuleiro[linha][coluna + 2]:
            vencedor = tabuleiro[linha][coluna]

    if count == 2:
        vencedor = tabuleiro[linha][coluna]

    return vencedor

def main():
    tam_matriz = int(input("Entre com o tamanho do tabuleiro: "))
    while tam_matriz > 10 or tam_matriz < 3:
        tam_matriz = int(input("dado invalido, entre novamente com o dado: "))

    matriz = crieMatriz(tam_matriz, " ")
    qnt_jogadores = int(input("Entre com a quantidade de jogadores: "))
    while qnt_jogadores > 5 or qnt_jogadores < 2:
        qnt_jogadores = int(input("dado invalido, entre novamente com o dado: "))

    vetor_jogadores = []
    for i in range(qnt_jogadores):
        aux = str(input("Entre com o nome do jogador {}: ".format(i+1)))
        temp = Jogador(aux, i+1)
        vetor_jogadores.append(temp)

    nome_arq = str(input("Entre com o caminho para o arquivo a qual deseja salvar os dados: "))
    arquivo = open(nome_arq, 'w')
    arquivo.write('Tamanho do tabuleiro = ' + str(tam_matriz) + '\n')
    arquivo.write('Quantidade de Jogadores = ' + str(qnt_jogadores) + '\n')
    for i in range(len(vetor_jogadores)):
        arquivo.write('Jogador ' + str(i+1) + ' = ' + vetor_jogadores[i].nome + '\n')
    print('Entre com as jogadas (id, linha, coluna)')
    arquivo.write('Jogadas (id, linha, coluna):' + '\n')

    jogadas = 1
    vencedor = -1
    while jogadas <= (len(matriz) ** 2):
        id_jogador, linha, coluna = input('jogada ' + str(jogadas) + ': ').split()
        linha = int(linha)
        coluna = int(coluna)
        while (linha >= tam_matriz or coluna >= tam_matriz) or matriz[linha][coluna] != " ":
            print('Jogada errada, tente novamente')
            id_jogador, linha, coluna = input('jogada ' + str(jogadas) + ': ').split()
            linha = int(linha)
            coluna = int(coluna)

        arquivo.write('Jogada ' + str(jogadas) + ': id=' + str(id_jogador) + ", linha=" + str(linha) + ", coluna=" + str(coluna) + '\n')
        matriz[linha][coluna] = id_jogador
        vencedor = verificaVencedor(matriz, linha, coluna)
        if vencedor != -1:
            vencedor = int(vencedor)
            vencedor -= 1
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
