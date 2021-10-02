continua = True

print('|-------------------------------------------------|')
print('|----------Inicializando o jogo da velha----------|')
print('|--Por favor entre com as configuracoes iniciais--|')
print('|-------------------------------------------------|\n')

# abrindo arquivo
salva = open(str(input("Nome do arquivo de dados: ")), 'w')

while continua:
    print('|-------------------------------------------------|')
    print('|--------------Iniciando uma partida--------------|')
    print('|------- Entre com os dados dessa partida --------|')
    print('|-------------------------------------------------|\n')
    tam_matriz, qnt_jogadores = map(int, input('Tamanho do tabuleiro e quantidade de jogadores: ').split())
    while tam_matriz > 10 or tam_matriz < 3 or qnt_jogadores > 5 or qnt_jogadores < 2:
        tam_matriz, qnt_jogadores = map(int, input('Dados invalidos tente novemente: ').split())

    salva.write(str(tam_matriz) + ' ' + str(qnt_jogadores) + '\n')

    matriz = []
    # criando a matriz que representa o tabuleiro
    for i in range(tam_matriz):
        aux = []
        for j in range(tam_matriz):
            aux.append('_')
        matriz.append(aux)

    nome_jogadores = []
    for i in range(qnt_jogadores):
        nome_jogadores.append(str(input("Nome do {} jogador: ".format(i + 1))))
        salva.write(nome_jogadores[i] + ' ' + str(i+1) + '\n')

    print()
    print('|-------------------------------------------------|')
    print('|----------------Iniciando o jogo-----------------|')
    print('|-------------------------------------------------|')
    print('|  Entrada de dados:                              |')
    print('|    -> Jogada i: (id, linha, coluna)             |')
    print('|-------------------------------------------------|')

    linha_separadora = ('|' + str("-" * ((len(matriz) * 4) + 2)) + '|')
    #imprimindo o tabuleiro
    print('Tabuleiro inicialmente:')
    print(linha_separadora)
    print('|  | ', end='')
    for i in range(len(matriz)):
        print(str(i), end=' | ')
    print()
    print(linha_separadora)
    for i in range(len(matriz)):
        print('| ' + str(i), end='| ')
        print(*matriz[i], sep = ' | ', end=' |\n')
        print(linha_separadora)
    print()

    jogadas = 1
    vencedor = -1
    max_jogadas = len(matriz) ** 2
    while jogadas <= max_jogadas:
        # lendo a jogada
        id_jogador, linha, coluna = map(int, input('Jogada ' + str(jogadas) + ': ').split())
        while (linha >= tam_matriz or coluna >= tam_matriz) or matriz[linha][coluna] != '_':
            print('Tente novamente', end=' ')
            id_jogador, linha, coluna = map(int, input('Jogada ' + str(jogadas) + ': ').split())

        salva.write(str(id_jogador) + ' ' + str(linha) + ' ' + str(coluna) + '\n')
        # colocando a jogada no tabuleiro
        matriz[linha][coluna] = id_jogador

        # verificando a jogada
        # horizontal e vertical
        count_h = 0
        count_v = 0
        for i in range (tam_matriz):
            for j in range (tam_matriz):
                if matriz[i][j] == matriz[linha][coluna]:
                    count_h += 1
                else:
                    count_h = 0

                if matriz[j][i] == matriz[linha][coluna]:
                    count_v += 1
                else:
                    count_v = 0

                if count_h > 2 or count_v > 2:
                    vencedor = matriz[linha][coluna]
                    break

            if count_h > 2 or count_v > 2:
                break
            else:
                count_h = 0
                count_v = 0

        if vencedor != -1:
            break

        # verificando diagonais
        count = 0
        for d in range (tam_matriz):
            for j in range (tam_matriz):
                if j + d >= tam_matriz:
                    break
                if matriz[j][j+d] == matriz[linha][coluna]:
                    count = count + 1
                else:
                    count = 0
                if count > 2:
                    vencedor = matriz[linha][coluna]
                    break
            if count > 2:
                break
            else:
                count = 0

        if vencedor != -1:
            break

        count = 0
        for d in range (tam_matriz):
            for j in range (tam_matriz):
                if j + d >= tam_matriz:
                    break
                if matriz[j+d][j] == matriz[linha][coluna]:
                    count = count + 1
                else:
                    count = 0
                if count > 2:
                    vencedor = matriz[linha][coluna]
                    break
            if count > 2:
                break
            else:
                count = 0

        if vencedor != -1:
            break

        count = 0
        for d in range (tam_matriz):
            for j in range (tam_matriz):
                if tam_matriz - 1 - d - j < 0:
                    break
                if matriz[j][tam_matriz - 1 - d - j] == matriz[linha][coluna]:
                    count = count + 1
                else:
                    count = 0
                if count > 2:
                    vencedor = matriz[linha][coluna]
                    break
            if count > 2:
                break
            else:
                count = 0

        if vencedor != -1:
            break

        count = 0
        for d in range (tam_matriz):
            for j in range (tam_matriz):
                if j + d >= tam_matriz:
                    break
                if matriz[tam_matriz - j - 1][j + d] == matriz[linha][coluna]:
                    count = count + 1
                else:
                    count = 0
                if count > 2:
                    vencedor = matriz[linha][coluna]
                    break
            if count > 2:
                break
            else:
                count = 0

        if vencedor != -1:
            break

        #imprimindo o tabuleiro
        print('\n' + linha_separadora)
        print('|  | ', end='')
        for i in range(len(matriz)):
            print(str(i), end=' | ')
        print()
        print(linha_separadora)
        for i in range(len(matriz)):
            print('| ' + str(i), end='| ')
            print(*matriz[i], sep = ' | ', end=' |\n')
            print(linha_separadora)
        print()

        jogadas += 1

    if vencedor != -1:
        vencedor -= 1

    print('\nTabuleiro final: ')
    print(linha_separadora)
    print('|  | ', end='')
    for i in range(len(matriz)):
        print(str(i), end=' | ')
    print()
    print(linha_separadora)
    for i in range(len(matriz)):
        print('| ' + str(i), end='| ')
        print(*matriz[i], sep = ' | ', end=' |\n')
        print(linha_separadora)
    print()

    if jogadas == (max_jogadas + 1):
        print('sem vencedor')
        salva.write('sem vencedor\n')
    else:
        print(nome_jogadores[vencedor] + ' venceu')
        salva.write(nome_jogadores[vencedor] + '\n')

    continua = (str(input('Voce deseja continuar jogando? [s/N] ')).lower() == 's')

salva.close()
