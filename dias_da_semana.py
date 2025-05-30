#Implemente um programa que leia um valor inteiro
#entre 1 e 7, correspondente ao dia da semana. O programa deve
#escrever o dia da semana por extenso correspondente ao valor
#lido. Por exemplo, se o usuário escrever 1, o programa deve exibir Domingo.

dia = int(input("Informe o dia da semana em números inteiros (1 a 7):"))
if dia < 1 or dia > 7 : print("Valor Inválido")
else:
  if dia == 1 : print("Domingo")
  if dia == 2 : print("Segunda")
  if dia == 3 : print("Terca")
  if dia == 4 : print("Quarta")
  if dia == 5 : print("Quinta")
  if dia == 6 : print("Sexta")
  if dia == 7 : print("Sabado")
