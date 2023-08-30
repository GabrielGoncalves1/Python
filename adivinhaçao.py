print('***********************')
print('* Jogo da adivinhação *')

total_de_tentativas = 3
numero_secreto = 42

while total_de_tentativas > 0:
    chute = int(input('Digite o seu número: '))

    if chute == numero_secreto:
        print('Você acertou!')
        break  # Se acertar, sair do loop
    elif chute > numero_secreto:
        print('Você digitou um valor muito alto')
    else:
        print('Você digitou um valor muito baixo')

    total_de_tentativas = total_de_tentativas - 1

if total_de_tentativas == 0:
    print('Suas tentativas acabaram. O número secreto era', numero_secreto)
