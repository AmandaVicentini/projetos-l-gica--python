import math

print('Digite o primeiro valor: ')
valor1 = float(input())
print('Digite o segundo valor: ')
valor2 = float(input())
print('Soma: ' , valor1+valor2)
print('Diferença: ' , valor1-valor2)
print('Média: ' , (valor1+valor2)/2)
print('Distancia: ' , math.fabs(valor1-valor2))
print('Maior: ' , (valor1+valor2+math.fabs(valor1-valor2))/2)
print('Menor: ' , (valor1+valor2-math.fabs(valor1-valor2))/2)
