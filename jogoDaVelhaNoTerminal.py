import os
gameOver = False
tipo = ''
error = False
jogadorDaVez = 1
ganhador = 0
marcados = [
    ' ',' ',' ',
    ' ',' ',' ',
    ' ',' ',' '
]
while gameOver == False:
    print('     A       B       C   ')
    print('         ∎       ∎       ')
    print('1    {}   ∎   {}   ∎   {}   '.format(marcados[0], marcados[1], marcados[2])) 
    print('         ∎       ∎       ') 
    print('  ∎ ∎ ∎ ∎ ∎ ∎ ∎ ∎ ∎ ∎ ∎ ∎')
    print('         ∎       ∎       ')
    print('2    {}   ∎   {}   ∎   {}   '.format(marcados[3], marcados[4], marcados[5])) 
    print('         ∎       ∎       ') 
    print('  ∎ ∎ ∎ ∎ ∎ ∎ ∎ ∎ ∎ ∎ ∎ ∎')
    print('         ∎       ∎       ')
    print('3    {}   ∎   {}   ∎   {}   '.format(marcados[6], marcados[7], marcados[8])) 
    print('         ∎       ∎       ') 
    print('---------------------------------')
    print('| Jogador 1: X  |  Jogador 2: O |')
    print('---------------------------------')
    if jogadorDaVez == 1:
        print('Vez do jogador 1!')
        tipo = 'X'
    elif jogadorDaVez == 2:
        print('Vez do jogador 2!')
        tipo = 'O'
    if error == True:
        print('ERROR! Não foi possível jogar na área em que você escolheu!')
        print('Escolha novamente!')
        error = False
    else:
        print('Diga qual coluna e linha você irá jogar ?')
    coluna = input('Coluna: ')
    linha = input('Linha: ')
    celula = coluna+linha
    if celula == 'A1':
        if marcados[0] == ' ':
            marcados[0] = tipo
        else:
            error = True
    elif celula == 'B1':
        if marcados[1] == ' ':
            marcados[1] = tipo
        else:
            error = True
    elif celula == 'C1':
        if marcados[2] == ' ':
            marcados[2] = tipo
        else:
            error = True
    elif celula == 'A2':
        if marcados[3] == ' ':
            marcados[3] = tipo
        else:
            error = True
    elif celula == 'B2':
        if marcados[4] == ' ':
            marcados[4] = tipo
        else:
            error = True
    elif celula == 'C2':
        if marcados[5] == ' ':
            marcados[5] = tipo
        else:
            error = True
    elif celula == 'A3':
        if marcados[6] == ' ':
            marcados[6] = tipo
        else:
            error = True
    elif celula == 'B3':
        if marcados[7] == ' ':
            marcados[7] = tipo
    elif celula == 'C3':
        if marcados[8] == ' ':
            marcados[8] = tipo
        else:
            error = True
    else:
        error = True

    #VERIFICANDO SE ALGUÉM GANHOU EM CADA LINHA 0 1 2 / 3 4 5 / 6 7 8
    if (marcados[0].isalpha() and ((marcados[0] == marcados[1]) and (marcados[1] == marcados[2]))):
        gameOver = True
        ganhador = jogadorDaVez
    elif (marcados[3].isalpha() and ((marcados[3] == marcados[4]) and (marcados[4] == marcados[5]))):
        gameOver = True
        ganhador = jogadorDaVez
    elif (marcados[6].isalpha() and ((marcados[6] == marcados[7]) and (marcados[7] == marcados[8]))):
        gameOver = True
        ganhador = jogadorDaVez
    #VERIFICANDO SE ALGUÉM GANHOU EM CADA COLUNA 0 3 6 / 1 4 7 / 2 5 8
    elif (marcados[0].isalpha() and ((marcados[0] == marcados[3]) and (marcados[3] == marcados[6]))):
        gameOver = True
        ganhador = jogadorDaVez
    elif (marcados[1].isalpha() and ((marcados[1] == marcados[4]) and (marcados[4] == marcados[7]))):
        gameOver = True
        ganhador = jogadorDaVez
    elif (marcados[2].isalpha() and ((marcados[2] == marcados[5]) and (marcados[5] == marcados[8]))):
        gameOver = True
        ganhador = jogadorDaVez
    #VERIFICANDO SE ALGUÉM GANHOU EM CADA DIAGONAL 0 4 8 / 2 4 6
    elif (marcados[0].isalpha() and ((marcados[0] == marcados[4]) and (marcados[4] == marcados[8]))):
        gameOver = True
        ganhador = jogadorDaVez
    elif (marcados[2].isalpha() and ((marcados[2] == marcados[4]) and (marcados[4] == marcados[6]))):
        gameOver = True
        ganhador = jogadorDaVez

    if error == False:
        if jogadorDaVez == 1:
            jogadorDaVez = 2
        elif jogadorDaVez == 2:
            jogadorDaVez = 1

    os.system('cls' if os.name == 'nt' else 'clear')

print('O Jogador {} venceu! :)'.format(ganhador))
print('')
print('     A       B       C   ')
print('         ∎       ∎       ')
print('1    {}   ∎   {}   ∎   {}   '.format(marcados[0], marcados[1], marcados[2])) 
print('         ∎       ∎       ') 
print('  ∎ ∎ ∎ ∎ ∎ ∎ ∎ ∎ ∎ ∎ ∎ ∎')
print('         ∎       ∎       ')
print('2    {}   ∎   {}   ∎   {}   '.format(marcados[3], marcados[4], marcados[5])) 
print('         ∎       ∎       ') 
print('  ∎ ∎ ∎ ∎ ∎ ∎ ∎ ∎ ∎ ∎ ∎ ∎')
print('         ∎       ∎       ')
print('3    {}   ∎   {}   ∎   {}   '.format(marcados[6], marcados[7], marcados[8])) 
print('         ∎       ∎       ') 