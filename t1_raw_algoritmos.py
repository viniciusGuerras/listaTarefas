class Tarefa:

    def __init__(self, id, desc, time):
        self.id = id
        self.desc = desc
        self.time = time
        self.status = True

    """usar o __str__ pra fazer um template de como a tarefa vai ser printada,
    dai na visualizacao nos podemos printar diretamente a tarefa, 
    ao invés de usar o print em cada elemento da tarefa (usar o __str__  para
    printar cada elemento bonitinho)
    """
    #PRINTAR TAMBEM O STATUS
    def __str__(self):
        pass
    
    def tarefaConcluida(self):
        self.status = False
        self.time = 0

    def getStatus(self):
        return self.status
    
#funcao pra fazer linha separatória bonitinha
def linhaDivisoria():
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    

#funcao que checa se a lista esta vazia ou nao (para ser usada na visualizacao)
def aListaTaVazia(listaDeTarefas):
    if len(listaDeTarefas) > 0:
        return False
    return True

#mudança no localizaIndentificador: agora ele retorna a posiçao do identificador na lista
def localizaIndentificador(listaDeTarefas, id):
    for posicao in range(len(listaDeTarefas)):
        if listaDeTarefas[posicao].id == id:
            return posicao;
    return None

def adiciona_tarefa(listaDeTarefas):

    linhaDivisoria()
    
    print("*****Nova-Tarefa*****")
    #FAZER checar se o indetificador que vai ser criado é um inteiro (se for string mostrar erro)
    id = input("Digite o identificador da tarefa: ")
    while localizaIndentificador(listaDeTarefas,id) != None:
        print("Uma tarefa com o mesmo identificador foi localizada.")
        id = input("Digite um novo identificador para a tarefa: ")
    
    #talvez fazer um outro while para conseguir dar um [ERRO] diferente 
    desc = input("Digite a descrição da tarefa: ")
    #FAZER mesma checagem para o tempo
    time = input("Digite o tempo limite da tarefa: ")

    tarefa = Tarefa(id, desc, time)
    listaDeTarefas.append(tarefa)
    print(f"Tarefa criada e adicionada com sucesso.")
   

def visualiza_tarefas(listaDeTarefas):
    
    #FAZER - detalhar a visualizacao de tarefas para separar individualmente elas e deixar bonitn (usar o __str__ na tarefa)
    linhaDivisoria()

    #checa o numero de tarefas que existem na lista
    numeroTarefas = len(listaDeTarefas)
    
    #menuzinho das tarefas
    print(f"Quantidade de tarefas: {numeroTarefas}")
    print("Opçōes de visualização:")
    print("\t1 - Todas")
    print("\t2 - Ativas")
    print("\t3 - Concluídas")

    #checa o input do usuario para o menu
    input_usuario = input()

    while int(input_usuario) > 4 or int(input_usuario) < 1:
        print("Opção inválida")
        input_usuario = input()

    """FAZER - usar a funcao alistatavazia pra checar se tem algo dentro, caso estiver vazia
    printar algo para o usuario""" 
    

    for task in listaDeTarefas:
        #faz a checagem para cada opcao de print
        if input_usuario == "1":
            print(f"\nidentificador da tarefa: {task.id}\ndescrição da tarefa: {task.desc}\ntempo da tarefa: {task.time}")
        elif input_usuario == "2":
            if task.getStatus():
                print(f"identificador da tarefa: {task.id}\ndescrição da tarefa: {task.desc}\ntempo da tarefa: {task.time}")
        elif input_usuario == "3":
            if not task.getStatus():
                print(f"identificadorda tarefa: {task.id}\ndescrição da tarefa: {task.desc}\ntempo da tarefa: {task.time}")

def atualiza_tarefas(listaDeTarefas):

    #FAZER - adicionar parte bonus (prioridade de tarefas)
    linhaDivisoria()
   
    identificador = input("Identificador da tarefa: ")
    #acha a posicao na lista da tarefa
    posicao_id = localizaIndentificador(listaDeTarefas, identificador)
    
    #caso a posicao existir:
    if(posicao_id != None):

        #pergunta qual e atualiza a informacao
        print("\nQual item deseja atualizar? ")
        print("\t1 - Descrição")
        print("\t2 - Tempo")

        input_usuario = input()

        while input_usuario != "1" and input_usuario != "2":
            print("Opção inválida")
            input_usuario = input()
            
        if input_usuario == "1":     
                    listaDeTarefas[posicao_id].desc = input("digite a nova descrição: ")
        elif input_usuario == "2":        
                    listaDeTarefas[posicao_id].time = input("digite o novo tempo: ")
        print("Tarefa atualizada!")
    #caso ela nao existir
    else:
        print("Tarefa não encontrada")

def conclui_tarefas(listaDeTarefas):

    linhaDivisoria()
    
    identificador = input("Identificador(es) da tarefa concluida: ")
    #acha a posicao do identificador na lista
    posicao_id =  localizaIndentificador(listaDeTarefas, identificador)
    #mensagem de aviso para caso queira prosseguir
    print(f"a tarefa será concluida!")
    print("continuar?")
    print("\t1 - sim")
    print("\t2 - não")
    opcao = input("")

    while(opcao != "1" and opcao != "2"):
        print("Opção inválida")
        opcao = input("Continuar? ")

    #caso prosseguir -> concluir tarefa
    if opcao == "1":
        if(posicao_id != None):
            listaDeTarefas[posicao_id].tarefaConcluida()
            #FAZER - depois de atualizar o __str__ podemos usar aqui
            print(f"A tarefa {listaDeTarefas[posicao_id].id}, descricao: {listaDeTarefas[posicao_id].desc} foi concluída")
        else:
            print("Tarefa não encontrada.")
    else:
        print("Alteração não efetuada")
    

def exclui_tarefas(listaDeTarefas):
    
    linhaDivisoria()

    identificador = input("Identificador da tarefa(s): ")
    


    posicao_id =  localizaIndentificador(listaDeTarefas, identificador)

    #mensagem aviso sobre exclusao de tarefa
    print(f"A tarefa não poderá ser recuperada após a remoção")
    print("Continuar?")
    print("\t1 - sim")
    print("\t2 - não")
    opcao = input("")

    while(opcao != "1" and opcao != "2"):
        print("Opção inválida")
        opcao = input("Continuar? ")
    
    #caso preosseguir -> excluir tarefa
    if opcao == "1":
        if(posicao_id != None):
            listaDeTarefas.pop(posicao_id)
            print("Tarefa removida com sucesso")
        else:
            print("Tarefa não encontrada")
    else:
        print("Exclusão não efetuada")
    

def menu_principal():

    listaDeTarefas = []

    while True:

        print("\n*** Sistema de Gerenciamento de Tarefas ***")
        print("Digite a opção desejada:")
        print("\t0 - Sair")
        print("\t1 - Adicionar tarefa")
        print("\t2 - Visualizar tarefas")
        print("\t3 - Atualizar tarefas")
        print("\t4 - Concluir tarefas")
        print("\t5 - Excluir tarefas")
        
        opcao = input()
        
        if opcao == "0":
            break
        if opcao == "1":
            adiciona_tarefa(listaDeTarefas)
        elif opcao == "2":
            visualiza_tarefas(listaDeTarefas)
        elif opcao == "3":
            atualiza_tarefas(listaDeTarefas)
        elif opcao == "4":
            conclui_tarefas(listaDeTarefas)
        elif opcao == "5":
            exclui_tarefas(listaDeTarefas)
        else:
            print("Opção inválida!")

menu_principal()