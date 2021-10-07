import random as rand

"""
alterando a forma como utiliza o print
de:
    print('Meu nome é {}'.format(nome))
para:
    print(f'Meu nome é {nome}')

~ Odair J.
"""


def jogar():

    print('*********************************')
    print('Bem-Vindo no jogo de Adivinhação!')
    print('*********************************')

    numero_secreto = int(rand.randrange(1,101))
    total_de_tentativas = int(0)
    pontos = int(1000)


    print('Qual nivel de dificuldade?\n (1) Fácil (2) Médio  (3) Difícil', numero_secreto)

    nivel = int(input('Define o nível: '))

    if(nivel == 1):
        total_de_tentativas = 20 
    elif(nivel == 2): 
        total_de_tentativas = 10
    else: 
        total_de_tentativas = 5 

    for rodada in range(1, total_de_tentativas + 1):
        print(f"Tentativa {rodada} de {total_de_tentativas}")

        # convertendo direto para inteiro, ja que não é necessario utilizar str
        # Não necessario mais  -> chute = int(chute_str)
        chute = int(input("Digite um número entre 1 e 100: "))
        print(f"Você digitou: {chute}")

        if(chute < 1 or chute > 100):
            print('Voce deve digitar um número entre 1 e 100!')
            continue # continuar com a proxima rodada
        
        acertou = chute == numero_secreto # é um tipo variável bool q pode ter 2 valores, true ou false.
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print(f'Voce acertou e fez {pontos} pontos!')
            # Possuia um erro nesta  linha 
            # print('Voce acertou e fez {] pontos!'.format(pontos))
            break
        else:
            if(maior):
                print('Voce errou! O seu chute foi maior do que o número secreto.')
            elif(menor):
                print('Voce errou! O seu chute foi menor do que o número secreto.')
            # Para poupar memoria esta variavel não é necessaria
            #pontos_perdidos = abs(numero_secreto - chute) 
            pontos = pontos - abs(numero_secreto - chute) 

            print('Fim de Jogo')
if (__name__ == '__main__'):
    jogar()
