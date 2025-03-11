import random
computador = random.randrange(1, 11) # A maquina gera um número
jogador = int(input("Tente adivinhar um número de 1 a 10: ")) # O jogador tenta adivinhar o número

tentativas = 1 # Variável para as tentativas, começando em 1 


while (computador != jogador): # LOOPING
    if (computador > jogador):
        print("ERRO! O número é maior!")
    elif (computador < jogador):
        print("ERRO! O número é menor!")
    tentativas = (tentativas + 1)
    jogador = int(input("Tente adivinhar um número de 1 a 10: "))
    
    
if (computador == jogador):
    print("PARABÉNS! O Número era " + str(jogador) + ", você acertou em " + str(tentativas) + " tentativas!")