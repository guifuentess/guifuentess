from random import randint
computador = randint (0,10)
print('''Sou seu computador... Acabei de pensar em um numero de 0 a 10. Sera que voce consegue advinhar qual foi\n''')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o palpite\n'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print ('Mais... Tente mais uma vez')
        elif jogador < computador:
            print ('Menos... Tente mais uma vez')
print ('Acertou com {} tentativas. Parabéns'
    .format (palpites))