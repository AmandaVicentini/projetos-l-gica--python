num = int(input("Informe um valor natural: "))
cont = 0
d = 1
while d <= num:
  if num % d == 0 : cont = cont + 1
  d = d + 1
if cont == 2 : print(num, "É primo")
else: print(num, "Não é primo")
