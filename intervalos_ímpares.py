a = int(input("Informe o valor inicial do intervalo: "))
while a<0:
  print("O valor inicial do intervalo deve ser um valor natural")
  a = int(input("Informe novamente o valor inicial do intervalo: "))

b = int(input("Informe o valor final do intervalo: "))
while b<0:
  print("O valor final do intervalo deve ser um valor natural")
  b = int(input("Informe novamente o valor final do intervalo: "))

if a > b:
  aux = a
  a = b
  b = aux

if a%2 == 0 : a = a + 1
soma = 0
print("Valores ímpares do intervalo: ")

while a <= b:
  print(a)
  soma = soma + a
  a = a + 2
print("Soma dos ímapres do intervalo: " , soma)
