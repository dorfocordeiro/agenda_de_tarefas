import os
import json

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
    listar(tarefas)


def refazer(tarefas, refazer_tarefa):
    if not refazer_tarefa:
        print('Nenhuma tarefa para refazer')
        return
    tarefa = refazer_tarefa.pop()
    tarefas.append(tarefa)
    print()
    listar(tarefas)

def adicionar(tarefa, tarefas):
    tarefa = tarefa.strip()
    if not tarefa:
        print('Nenhuma tarefa digitada.')
        return
    tarefas.append(tarefa)
    print()
    listar(tarefas)

def ler(tarefas,diretorio):
    dados = []
    try:
        with open(diretorio, 'r', encoding='utf8') as file:
            dados = json.load(file)
    except FileNotFoundError:
        print('Arquivo não encontrado')
        salvar(tarefas, diretorio)
    return dados


def salvar(tarefas, diretorio):
        dados = tarefas
        with open(diretorio, 'w', encoding='utf8') as file:
            dados = json.dump(tarefas, file, indent=2, ensure_ascii=False)
        return dados
    

DIRETORIO = 'diretorio.json'
tarefas = ler([], DIRETORIO)
refazer_tarefa = []


while True:
# PARA MELHORAR O CODIGO COM OS IF

    print('Comandos: listar, desfazer ou refazer')
    tarefa = input('Adicione uma tarefa ou digite os comandos: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, refazer_tarefa),
        'refazer': lambda: refazer(tarefas, refazer_tarefa),
        'clear': lambda: os.system('clear'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']
    comando()
    salvar(tarefas, DIRETORIO)
