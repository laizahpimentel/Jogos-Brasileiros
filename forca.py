
def jogar():
    print('*********************************')
    print('***Bem-Vindo no jogo da Forca!***')
    print('*********************************')

    palavra_secreta = 'banana'

    enforcou = False
    acertou = False

    # enquanto não false e não false
    while(not enforcou and not acertou):
        
        chute = input('Qual letra?')
        chute = chute.strip ()
        index = 0 
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper ()):
                print('Encontrei a letra {} na posição {}'.format(letra, index))      
            index = index + 1 
        print('Jogando ...')

    print('Fim de Jogo')

if(__name__=='__main__'):
    jogar() 


