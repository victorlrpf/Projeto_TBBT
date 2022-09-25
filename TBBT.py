# Criar um Pedra, Papel, Tesoura, Lagarto e Spock
# Tesoura corta papel, papel cobre a pedra, pedra esmaga o lagarto, o lagarto envenena o spock, spock quebra a tesoura.
# A tesoura mata o lagarto, o lagarto come o papel, o papel refuta o spock, o spock vaporiza a pedra, pedra amassa a tesora.

from random import randint

escolhas = ('Pedra', 'Papel', 'tesoura', 'lagarto', 'Spock')
sheldon = randint(0,4)

print('''Esolha uma opção 
[0] Pedra
[1] Papel
[2] Tesoura
[3] Lagarto
[4] Spock''')

jogador = int(input('Qual vai escolher?  '))

print ("-=" * 20)
print ('O Sheldon Jogou {}',format(escolhas[sheldon]))
print ('O jogador jogou {}',format(escolhas[jogador]))
print ("-=" * 20)

if sheldon == 0: #pedra

    if jogador == 0:
        print('Empatou')

    elif jogador == 1:
        print("jogador Venceu")
    elif jogador == 2:
        print("Sheldon Venceu")
    elif jogador == 3:
        print("Sheldon venceu")
    elif jogador == 4:
        print("jogador Venceu")
    else:
        print('Jogada invalida amigão')
elif sheldon == 1: #papel
    if jogador == 0:
        print("Sheldon venceu")
    elif jogador == 1:
        print("Empatou")
    elif jogador == 2:
        print("jogador venceu")
    elif jogador == 3:
        print("jogador venceu")
    elif jogador == 4:
        print("Sheldon venceu")
    else:
        print('Jogada invalida amigão')

elif sheldon == 2: #tesoura
    if jogador == 0:
        print("jogador venceu")
    elif jogador == 1:
        print("Sheldon venceu")
    elif jogador == 2:
        print("Empatou")
    elif jogador == 3:
        print("Sheldon venceu")
    elif jogador == 4:
        print("jogador venceu")
    else:
        print('Jogada invalida amigão')

elif sheldon == 3: #lagarto
    if jogador == 0:
        print("jogador venceu")
    elif jogador == 1:
        print("Sheldon venceu")
    elif jogador == 2:
        print("jogador venceu")
    elif jogador == 3:
        print("Empate")
    elif jogador == 4:
        print("Sheldon venceu")
    else:
        print('Jogada invalida amigão')

elif sheldon == 4: #spock
    if jogador == 0:
        print("Sheldon venceu")
    elif jogador == 1:
        print("jogador venceu")
    elif jogador == 2:
        print("Sheldon venceu")
    elif jogador == 3:
        print("jogador venceu")
    elif jogador == 4:
        print("Empatou")
    else:
        print('Jogada invalida amigão')