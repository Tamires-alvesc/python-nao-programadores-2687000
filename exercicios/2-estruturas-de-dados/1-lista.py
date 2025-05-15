# Crie uma lista apenas com elementos numéricos
numeros = [2, 7, 9.76, 35, 890, 76, 9]
# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
lista = ['Tamires', 123, [1,2,3], 1.23, {'nome': 'Tamires', 'idade': 30}, True, False]
# Imprima na tela apenas os 5 primeiros elementos da lista
print(numeros[:5])
print(lista[:5])

# Crie um slice na lista para que imprima na tela os elementos de índice par
print(numeros[::2])
print(lista[::2])
# Remova da lista o último item
numeros.pop()
lista.pop()
# Insira na lista um novo item
numeros.append(10)
lista.append('Oi')
print(numeros)
print(lista)
# Remova da lista um item específico
numeros.remove(7)
lista.remove(1.23)
print(numeros)
print(lista)
