# Declare 4 variáveis do tipo numérica
a = 0
b = 2.5
c = 8
d = 4.98

# Crie uma estrutura condicional para comparar dois números
# Se a condição for verdadeira, imprima na tela uma mensagem informando que a condição foi cumprida e informando o número de maior valor
# Se a condição não for cumprida, imprima na tela uma mensagem informando que a condição é negativa e informe o número de maior valor
# Insira outras condições na estrutura condicional usando o elif
if a > b:
  print(f'Condição cumprida. O valor {a} é maior do que o valor {b}')
elif a < b:
  print(f'Condição negativa. O valor {b} é maior do que o valor {a}')
elif a == b:
  print('Valores são iguais')
# Incremente a estrutura condicional já existente com expressões lógicas utilizando "and" ou "or"
if (a > b) and (c!= 0):
  print(f'Condição cumprida. O valor {a} é maior do que o valor {b} e {c} é diferente de zero')
elif (a < b) or (d == 0):
  print(f'Condição negativa. O valor {b} é maior do que o valor {a} ou {d} é igual a zero')
else:
  print('As condições não foram cumpridas')

# Crie uma estrutura condicional onde mais de uma condição seja verdadeira, e use apenas a palavra reservada "if"
