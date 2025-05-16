# Crie uma função para selecionar o curso desejado em uma trilha profissional
def selecionar_curso():
  opcao = int(input('Escolha uma opção:\n 1 - Gestão de Projetos\n 2 - Excel Básico\n 3 - Python Iniciante : \n'))
  print(f'Você escolheu o curso {opcao}')
  return opcao
# Crie uma função para percorrer todos os níveis de um curso e imprimir na tela a informação do nível atual

def percorrer_curso(curso_selecionado):
  trilha = {1: {'título': 'Gestão de Projetos', 'total_níveis': 3}, 2: {'título': 'Excel Básico', 'total_níveis': 6}, 3: {'título': 'Python Iniciante', 'total_níveis': 4}} 

  curso_atual = trilha[curso_selecionado]['título']
  curso_nível_atual = 1
  curso_total_níveis = trilha[curso_selecionado]['total_níveis']

  print(f'Bem vinda ao curso "{curso_atual}"!. Você está iniciando o curso no nível {curso_nível_atual}.\n........')
        
  while curso_nível_atual <= curso_total_níveis:
      print(f'Parabéns! Você acaba de finalizar a fase {curso_nível_atual} do curso "{curso_atual}".')
      curso_nível_atual += 1
  else:
      print(f'Você concluiu o {curso_atual} com sucesso!!')

# Execute as funções
curso = selecionar_curso()
percorrer_curso(curso)
        


