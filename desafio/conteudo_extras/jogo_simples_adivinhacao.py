import random
import os

erros = 0
num_sorteado = random.randrange(0, 50)
print("Voce tem 5 tentativas!\nTentativa: ", erros + 1)
num_jogador = int(input('Digite um numero de 0 a 50: '))

while (erros + 1) < 5:
    os.system('cls')
    if num_sorteado > num_jogador:
        print("Erro! O numero sorteado e maior do que voce digitou!")
        erros += 1
        print("Erro numero: ", erros)
    elif num_sorteado < num_jogador:
        print("Erro! O numero sorteado e menor do que voce digitou!")
        erros += 1
        print("Erro numero: ", erros)        
    else:
        print(f"Voce Acertou!!!\nO numero digitado: {num_jogador} e igual ao numero sorteado: {num_sorteado}.")
        print("Tentativas: ", erros + 1)
        break
    print("Tentativa: ", erros + 1)
    num_jogador = int(input('Digite um numero de 0 a 50: '))
    os.system('cls')
print("Voce perdeu!!!\n")
