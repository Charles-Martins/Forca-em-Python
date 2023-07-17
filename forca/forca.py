import random

palavras = ['python', 'programacao', 'computador', 'desenvolvimento', 'jogos']
escolhida = random.choice(palavras)
letras_erradas = []
letras_corretas = []
tentativas = 6

def exibir_forca(tentativas):
    fases = [
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |
        ''',
        '''
           --------
           |      |
           |      O
           |
           |
           |
        ''',
        '''
           --------
           |      |
           |
           |
           |
           |
        '''
    ]
    return fases[tentativas]

def exibir_palavra(palavra, letras_corretas):
    exibicao = ''
    for letra in palavra:
        if letra in letras_corretas:
            exibicao += letra + ' '
        else:
            exibicao += '_ '
    return exibicao

def jogar():
    global tentativas 

    print('Bem-vindo ao Jogo da Forca!')
    print(exibir_forca(tentativas))
    print(exibir_palavra(escolhida, letras_corretas))

    while True:
        palpite = input('\nDigite uma letra: ').lower()

        if len(palpite) != 1:
            print('Digite apenas uma letra por vez!')
            continue

        if palpite in letras_corretas or palpite in letras_erradas:
            print('Você já tentou essa letra. Tente outra.')
            continue

        if palpite in escolhida:
            letras_corretas.append(palpite)
        else:
            letras_erradas.append(palpite)
            tentativas -= 1

        print(exibir_forca(tentativas))
        print(exibir_palavra(escolhida, letras_corretas))

        if tentativas == 0:
            print('Você perdeu! A palavra correta era:', escolhida)
            break

        if all(letra in letras_corretas for letra in escolhida):
            print('Parabéns, você acertou a palavra!')
            break

jogar()
