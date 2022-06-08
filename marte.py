def cadastrarSonda():
    posicao_inicial_x, posicao_inicial_y, direcao_inicial = input(
        "Informe sua posição inicial (Input de 3 valores: x, y e direção inicial(N, S, W, E) ): ").split()
    posicao_inicial_x = int(posicao_inicial_x)
    posicao_inicial_y = int(posicao_inicial_y)

    movimentos = input("Informe seu comando de movimento: ")
    movimentos = list(movimentos)
    return (posicao_inicial_x, posicao_inicial_y, direcao_inicial, movimentos)


def movimentarSondas(malha_x, malha_y, posicao_x, posicao_y, direcao, movimentos):

    for movimento in movimentos:
        # Rotação LEFT
        direcao = direcao.upper()
        movimento = movimento.upper()

        if (movimento == 'L'):
            if (direcao == 'N'):
                direcao = 'W'
            elif (direcao == 'W'):
                direcao = 'S'
            elif (direcao == 'S'):
                direcao = 'E'
            elif (direcao == 'E'):
                direcao = 'N'

        # Rotação RIGHT
        elif (movimento == 'R'):
            if (direcao == 'N'):
                direcao = 'E'
            elif (direcao == 'E'):
                direcao = 'S'
            elif (direcao == 'S'):
                direcao = 'W'
            elif (direcao == 'W'):
                direcao = 'N'
        # Movimentos
        elif (movimento == 'M'):
            if (direcao == 'N'):
                posicao_y += 1
            elif (direcao == 'S'):
                posicao_y -= 1

            if(direcao == 'W'):
                posicao_x -= 1
            elif(direcao == 'E'):
                posicao_x += 1

            # PREVININDO QUE PASSE DA MALHA
            if (posicao_y < 0):
                posicao_y += 1
                print('Não posso seguir por esse caminho')
                break

            elif(posicao_y > malha_y):
                posicao_y -= 1
                print('Não posso seguir por esse caminho')
                break

            if(posicao_x < 0):
                posicao_x += 1
                print('Não posso seguir por esse caminho')
                break

            elif(posicao_x > malha_x):
                posicao_x -= 1
                print('Não posso seguir por esse caminho')
                break

    return(print(posicao_x, posicao_y, direcao))


# Recebendo INPUT
x, y = input(
    "Defina coordenada do ponto superior-direito (Input de 2 valores): ").split()
x = int(x)
y = int(y)

sonda_um_posicao_inicial_x, sonda_um_posicao_inicial_y, sonda_um_direcao_inicial, sonda_um_movimentos = cadastrarSonda()

sonda_dois_posicao_inicial_x, sonda_dois_posicao_inicial_y, sonda_dois_direcao_inicial, sonda_dois_movimentos = cadastrarSonda()

movimentarSondas(x, y, sonda_um_posicao_inicial_x, sonda_um_posicao_inicial_y,
                 sonda_um_direcao_inicial, sonda_um_movimentos)


movimentarSondas(x, y, sonda_dois_posicao_inicial_x, sonda_dois_posicao_inicial_y,
                 sonda_dois_direcao_inicial, sonda_dois_movimentos)

print(movimentarSondas)
