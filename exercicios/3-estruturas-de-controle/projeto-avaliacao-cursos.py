# Nesse desafio você verificará dentro de uma lista se o item está contido nela,
#  caso verdadeiro deverá imprimir na tela essa informação, 
# além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.

# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
cursos = ['Liderança', 'Gestão de Projetos', 'Power BI', 'Excel Básico', 'Python Iniciante']

# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
a = 'Liderança'
b = 'Gestão de Pessoas'
c = 'Excel Básico'

# 3. Crie um dicionário vazio para armazenar a nota do curso
notas = dict()
# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota

if a in cursos:
  nota_a = float(input(f'Nota para o curso {a}:'))
  notas[a] = nota_a
else:
  print(f'Esse curso {a} não está na lista')

if b in cursos:
  nota_b = float(input(f'Nota para o curso {b}:'))
  notas[b] = nota_b
else:
  print(f'Esse curso {b} não está na lista')

if c in cursos:
  nota_c = float(input(f'Nota para o curso {c}:'))
  notas[c] = nota_c
else:
  print(f'Esse curso {c} não está na lista')

print(notas)