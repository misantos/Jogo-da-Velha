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
    print()
    linha = "-" * ((len(matriz) * 4) - 1)
    for i in range(len(matriz) - 1):
        print("", end=" ")
        print(*matriz[i], sep = " | ")
        print(linha)

    print("", end=" ")
    print(*matriz[-1], sep = " | ")

def verificaVencedor(tabuleiro):
    count = 1
    ref = tabuleiro[0][0]
    for i in range(len(tabuleiro)):
        if tabuleiro[i][i] != ref:
            ref = tabuleiro[i][i]
            count = 1
        else:
            count += 1

        if count == 3:
            return ref

    count = 1
    ref = tabuleiro[0][-1]
    for i in range(len(tabuleiro)):
        if tabuleiro[i][-i] != ref:
            ref = tabuleiro[i][i]
            count = 1
        else:
            count += 1

        if count == 3:
            return ref






def main():
    tam_matriz = int(input("Entre com o tamanho do tabuleiro: "))
    while tam_matriz > 10 or tam_matriz < 3:
        tam_matriz = int(input("dado invalido, entre novamente com o dado: "))

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
    arquivo.write('Jogadas: (id, linha, coluna)')



    matriz = crieMatriz(tam_matriz, " ")
    printMatriz(matriz)
    arquivo.close()

main()
