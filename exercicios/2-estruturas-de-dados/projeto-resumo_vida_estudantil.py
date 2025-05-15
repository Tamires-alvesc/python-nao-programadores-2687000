# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
nome = input('Entre com o nome:')
ano_link = int(input('Ano em que conheceu o LinkedIn:'))
ano_atual = int(input('Ano atual:'))
cursos = input('Cursos realizados no LinkedIn Learning (separados por vírgula e em ordem cronológica):')
lista_curso = cursos.split(',')

# 2. Armazene esses dados em um dicionário
dados = dict()
dados['nome'] = nome
dados['ano_linkedin'] = ano_link
dados['ano_atual'] = ano_atual
dados['cursos'] = lista_curso
print(dados)

# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcorridos, total de cursos realizados e (apenas) o primeiro e último curso.
print('-'*40)
print('Informações da estudante:'.center)
print('-'*40)
print(f'Nome: {dados["nome"]}')
print(f'Ano em que conheceu o LinkedIn: {dados["ano_linkedin"]}')
print(f'Total de anos transcorridos: {dados["ano_atual"] - dados["ano_linkedin"]}')
print(f'Total de cursos realizados:{len(lista_curso)}')
print(f'Primeiro e último cursos: {dados["cursos"][0]} e {dados["cursos"][len(lista_curso)-1]} ')