import os

print('----Lista de tarefas----')

def listar(tarefas):
    if not tarefas:
        print('Nenhuma tarefa')
        return
    print('Tarefas: ')
    for tarefa in tarefas:
        print(f'{tarefa}')
    print()

def desfazer(tarefas, refazer_tarefa):
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return
    tarefa = tarefas.pop()
    refazer_tarefa.append(tarefa)
    print()

def refazer(tarefas, refazer_tarefa):
    if not refazer_tarefa:
        print('Nenhuma tarefa para refazer')
        return
    tarefa = refazer_tarefa.pop()
    tarefas.append(tarefa)
    print()

def adicionar(tarefa, tarefas):
    tarefa = tarefa.strip()
    if not tarefa:
        print('Nenhuma tarefa digitada.')
        return
    tarefas.append(tarefa)
    print()

tarefas = []
refazer_tarefa = []

while True:
    
    print('Comandos: listar, desfazer ou refazer')
    tarefa = input('Adicione uma tarefa ou digite os comandos: ')
    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, refazer_tarefa)
        listar(tarefas)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, refazer_tarefa)
        listar(tarefas)
        continue
    elif tarefa == 'clear':
        os.system('cls')
        continue
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue
        
