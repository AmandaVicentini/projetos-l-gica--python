#preço unitário de custo preço de venda
#valor abaixo de R$ 10,00 lucro de 70%
#de R$ 10,00 a menos de R$ 30,00 lucro de 50%
#de R$ 30,00 a menos de R$ 50,00 lucro de 40%
#valor acima ou igual a R$ 50,00 lucro de 30%

preco = float(input("Informe o preco de custo:"))
if preco < 0 : print("Valor Inválido!")
else :
  if  preco < 10 : venda = preco + preco * 0.7     #preço do produto + preço vezes 0,7(70%)
  if preco >= 10 and preco < 30 : venda = preco + preco * 0.5
  if preco >= 30 and preco < 50 : venda = preco + preco * 0,4
  if preco >= 50 : venda = preco + preco * 0,3
  print("Preço de venda:" , venda)
