import random

def jogar():

    print('*********************************')
    print('Bem-Vindo no jogo de Adivinhação!')
    print('*********************************')

    numero_secreto = random.randrange(1,101) 
    total_de_tentativas = 0
    pontos = 1000


    print('Qual nivel de dificuldade?', numero_secreto)
    print('(1) Fácil (2) Médio  (3) Difícil')

    nivel = int(input('Define o nível: '))
    if(nivel == 1):
        total_de_tentativas = 20 
    elif(nivel == 2):
        total_de_tentativas = 10
    else: 
        total_de_tentativas = 5 

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print('Voce deve digitar um número entre 1 e 100!')
            continue # continuar com a proxima rodada
        
        acertou = chute == numero_secreto # é um tipo variável bool q pode ter 2 valores, true ou false.
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print('Voce acertou e fez {] pontos!'.format(pontos))
            break
        else:
            if(maior):
                print('Voce errou! O seu chute foi maior do que o número secreto.')
            elif(menor):
                print('Voce errou! O seu chute foi menor do que o número secreto.')
            pontos_perdidos = abs(numero_secreto - chute) 
            pontos = pontos - pontos_perdidos

            print('Fim de Jogo')
if (__name__=='__main__'):
    jogar()


