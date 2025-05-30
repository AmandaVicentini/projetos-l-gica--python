print('Informe o tempo do evento em segundos: ')
tempo = int(input())
horas = tempo//3600
print('Horas: ' , horas)
resto = tempo%3600
minutos = resto//60
print('Minutos: ' , minutos)
segundos = resto % 60
print('Segundos: ' , segundos)
