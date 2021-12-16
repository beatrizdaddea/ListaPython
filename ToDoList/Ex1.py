"""
Faça uma lista de tarefas com as seguintes opções:
    -adicionar tarefa
    -listar tarefas
    -opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    -opção de refazer (a cada vez que chamarmos, refaz a última ação)
"""



def menu():
    print("")
    print(" 1- Montar To Do List  ")
    print(" 2- Desfazer última tarefa ")
    print(" 3- Refazer a última tarefa ")
    print(" 4- Ver sua To Do List ")
    print(" 5- Sair ")
    print("")
    

def listar_tarefa(lista): 
    for listagem, atividade  in enumerate(lista):
     print(f'{listagem + 1}. {atividade}')

def excluir_tarefa(lista): 
    tarefa = lista.pop()
    print(f' A tarefa"{tarefa}" foi excluída de sua To Do List')
    return tarefa

def incluir_tarefa(lista, tarefa):
    lista.append(tarefa)
    print(f"A tarefa: {tarefa}, foi adicionada em sua To Do List")

if __name__ == '__main__':
    lista = []
    

menu()

while True:
    opcao = input("\nEscolha uma opção entre 1 e 5: ")
    
    if opcao == '1':
        tarefa = input("Adicione uma tarefa:  ")
        incluir_tarefa(lista, tarefa)
       
    elif opcao == '2':
        ultima_tarefa = excluir_tarefa(lista)
    
    elif opcao == '3':
        if ultima_tarefa is None:
            print('Não há tarefa a ser refeita')
        else:
            incluir_tarefa(lista, ultima_tarefa)
   
    elif opcao == '4':
        if not lista:
            print('Não há tarefa a ser exibida')
        else:
         listar_tarefa(lista)
    
    elif opcao == '5':
        exit()
    else:
        print("Opção inválida! Escolha uma número entre 1 e 5.")
