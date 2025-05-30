# Exercício 1

# Jogo da adivinhação
# - 10 tentativas para adivinhar um número sorteado entre 1 e 100
# - Computador informa se o número é maior ou menor que o digitado

import random

sorteado = random.randint(1,100)

acertou = False

for tent in range(1,11):   #número de tentativas até 10 (sempre -1 pq começa a contar do 0)
  print(f"Tentativa {tent}: ", end="")   #end="" serve para a resposta ficar na mesma linha
  num = int(input())
  if num < sorteado:
    print("Tente um número maior")
  elif num > sorteado:
    print("Tente um número menor")
  else:
    acertou = True
    break   #Após acabarem as 10 tentativas, o jogo para

if acertou:
  print("Parabéns! Você acertou.")
else:
  print(f"Que pena, você perdeu. O número sorteado era {sorteado}")
