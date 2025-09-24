lista = []

while True:
    usuario = {}
    usuario['nome'] = input('Digite o nome do aluno: ')
    usuario['idade'] = int(input('Digite a idade do aluno: '))
    lista.append(usuario)
      
    continuar = input('Deseja continuar? (S/N): ').strip().upper()
    if continuar == 'N':
        break

print(f'Lista dos alunos: {lista}')
