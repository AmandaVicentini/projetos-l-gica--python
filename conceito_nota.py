# Determinar conceito de um aluno em função da sua nota:
# Maior ou igual a 90 - Conceito A
# Entre 80 e 90 (não incluindo) - Conceito B
# Entre 70 e 80 (não incluindo) - Conceitpo C
# Entre 60 e 70 (não incluindo) - Conceito D
# Menor que 60 - Conceito F

nota = int(input("Nota:"))
if nota >= 90 :
  print("Conceito A")
else:
  if nota >= 80 and nota < 90 :
    print("Conceito B")
  else:
    if nota >=70 and nota <80 :
      print("Conceito C")
    else:
      if nota >=60 and nota < 70 :
        print("Conceito D")
      else:
          print("Conceito F") #aqui não precisa colocar if nota < 60, pq é a unica que falta, então se não for nenhuma opção acima, ja se entende que é o Conceito
