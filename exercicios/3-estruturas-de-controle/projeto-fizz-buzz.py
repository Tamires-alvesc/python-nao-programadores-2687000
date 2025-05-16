# Criaremos um programa para substituir números por palavras em uma lista
# 1. Crie uma lista com 15 números
lista = [3, 7, 2, 0, 8, 19, 89, 90, 46, 78, 34, 92, 11, 27, 58]
# 2. Crie um for loop para percorrer todos os elementos da lista
# 3. Crie uma estrutura condicional para verificar cada número da lista:
# 3.1 Caso o número seja divisível por 3, substitua-o por "Fizz"
# 3.2 Caso o número seja divisível por 5, substitua-o por "Buzz"
# 3.3 Caso o número seja divisível por 3 e 5, substitua-o por "FizzBuzz"
indice = 0

for item in lista:
  if (item % 3 == 0) and (item % 5 == 0):
    lista[indice] = 'FizzBuzz' 
  elif item % 3 == 0:
    lista[indice] = 'Fizz'
  elif item % 5 == 0:
    lista[indice] = 'Buzz'
  else:
    lista[indice] = item
  indice += 1

print(lista)
