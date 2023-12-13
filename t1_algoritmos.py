class Tarefa:
    def __init__(self, id, title, desc, time):
        self.id = id
        self.title = title
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

        statusAtual = "Ativa" if  self.getStatus() else "Concluida"
        return (
            '---------------------------------------' +
            '\nIdentificador da tarefa: ' +str(self.id)+
            '\nTítulo da tarefa: ' +str(self.getTitle())+
            '\nDescrição: ' +str(self.desc)+
            '\nTempo: ' +str(self.time)+ ' horas'
            '\nSituação: ' + statusAtual
        )

    def tarefaConcluida(self):
        self.status = False
        self.time = 0

    def getTitle(self):
        return self.title

    def getStatus(self):
        return self.status

    def getTime(self):
        return int(self.time)

#funcao pra fazer linha separatória bonitinha
def linhaDivisoria():
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
   
#funcao que checa se a lista esta vazia ou nao (para ser usada na visualizacao)

def aListaTaVazia(listaDeTarefas):
    if len(listaDeTarefas) > 0:
        return False
    return True

#Função para verificar se o input fornecido é um inteiro ou não
def inteiro(inputUser):
    try:
        intValue = int(inputUser)
        return True
    except ValueError:
        return False

#colorizacao do texto pq sim
def tituloMensagem(mensagem):
    print(f"\033[95m{mensagem}\033[0m")

def erroMensagem(mensagem):
    print(f"\033[91m[ERRO]\033[0m - {mensagem}")

def avisoMensagem(mensagem):
    print(f"\033[93m[AVISO]\033[0m - {mensagem}")

def sucessoMensagem(mensagem):
    print(f"\033[92m{mensagem}\033[0m ")

#mudança no localizaIndentificador: agora ele retorna a posiçao do identificador na lista
def localizaIndentificador(listaDeTarefas, id):
    for posicao in range(len(listaDeTarefas)):
        if listaDeTarefas[posicao].id == id:
            return posicao
    return None

def adiciona_tarefa(listaDeTarefas):
    linhaDivisoria()

    tituloMensagem("*****Nova-Tarefa*****")

    #FAZER checar se o indetificador que vai ser criado é um inteiro (se for string mostrar erro)
    #FEITO. Criei uma função para conferir
    id = input("Digite o identificador da tarefa: ")

    while inteiro(id) == False:
        erroMensagem("O identificador precisa ser um número inteiro.")
        id = input("Digite um novo identificador: ")

    while localizaIndentificador(listaDeTarefas,id) != None:
        erroMensagem("Uma tarefa com o mesmo identificador foi localizada.")
        id = input("Digite um novo identificador para a tarefa: ")
   
    #talvez fazer um outro while para conseguir dar um [ERRO] diferente
    title = input("Digite o título da tarefa: ")
    desc = input("Digite a descrição da tarefa: ")
    #feito usando a mesma função para checagem do id
    time = input("Digite o tempo limite da tarefa: ")

    while inteiro(time) == False:
        print("O tempo precisa ser um valor numérico.")
        time = input("Digite o tempo limite da tarefa: ")

    tarefa = Tarefa(id, title, desc, time)
    listaDeTarefas.append(tarefa)
    sucessoMensagem(f"Tarefa {tarefa.getTitle()} criada e adicionada com sucesso.")

def prioridade_lista(listaDeTarefas):
    listaAtiva = [tarefa for tarefa in listaDeTarefas if tarefa.getStatus()]
    listaAtivaSorted = sorted(listaAtiva, key= lambda tarefa : tarefa.getTime())
    return listaAtivaSorted

def visualiza_tarefas(listaDeTarefas):

    if aListaTaVazia(listaDeTarefas):
        erroMensagem("Não há tarefas adicionadas.")
    else:
        #checa o numero de tarefas que existem na lista
        numeroTarefas = len(listaDeTarefas)
    
        #menuzinho das tarefas
        print(f"Quantidade de tarefas: {numeroTarefas}")
        print("Opçōes de visualização:")
        print("\t1 - Todas")
        print("\t2 - Ativas")
        print("\t3 - Concluídas")
        #adicionei a opcao simples que vai printar apenas o titulo e a situacao
        print("\t4 - Simples")
        #checa o input do usuario para o menu
    
        input_usuario = input()
    
        linhaDivisoria()
        while int(input_usuario) > 4 or int(input_usuario) < 1 or not input_usuario.isnumeric():
            print("Opção inválida")
            input_usuario = input()

        #faz a checagem para cada opcao de print
        lista = []
        if input_usuario == "1":
            lista = prioridade_lista(listaDeTarefas)
            for task in lista:
                    print(task)
            for task in listaDeTarefas:
                listaFinal = [task for task in listaDeTarefas if task not in lista]
            for tarefa in listaFinal:
                print(tarefa)
        for task in listaDeTarefas:
            if input_usuario == "2":
                lista = prioridade_lista(listaDeTarefas)
                for task in lista:
                    print(task)
            if input_usuario == "3":
                if not task.getStatus():
                    print(task)
            elif input_usuario == "4":
                statusAtual = "Ativa" if task.getStatus() else "Concluida"
                print(f"Tarefa: {task.getTitle()}, situação: {statusAtual}")

def atualiza_tarefas(listaDeTarefas):

    if aListaTaVazia(listaDeTarefas):
        erroMensagem("Não há tarefas adicionadas.")

    else:
        linhaDivisoria()
        identificador = input("Identificador da tarefa: ")
        #acha a posicao na lista da tarefa
        posicao_id = localizaIndentificador(listaDeTarefas, identificador)
    
        #caso a posicao existir:
        if(posicao_id != None):

            #pergunta qual e atualiza a informacao
            print("\nQual item deseja atualizar? ")
            print("\t1 - Título")
            print("\t2 - Descrição")
            print("\t3 - Tempo")
            #Acrescentei o título aqui

            input_usuario = input()

            while int(input_usuario) < 1 or int(input_usuario) > 3:
                    erroMensagem("Opção inválida")
                    input_usuario = input()
            if input_usuario == "1":
                        listaDeTarefas[posicao_id].title = input("Digite o novo título: ")
            elif input_usuario == "2":    
                        listaDeTarefas[posicao_id].desc = input("Digite a nova descrição: ")
            elif input_usuario == "3":        
                        listaDeTarefas[posicao_id].time = input("digite o novo tempo: ")
            
            sucessoMensagem("Tarefa atualizada!")
        #caso ela nao existir
        else:
            erroMensagem("Tarefa não encontrada")

def conclui_tarefas(listaDeTarefas):
    if aListaTaVazia(listaDeTarefas):
        erroMensagem("Não há tarefas adicionadas.")
    else:
        linhaDivisoria()
        identificador = input("Identificador da tarefa concluida: ")
        #acha a posicao do identificador na lista
        posicao_id =  localizaIndentificador(listaDeTarefas, identificador)
        #mensagem de aviso para caso queira prosseguir
        if posicao_id != None:
            avisoMensagem(f"a tarefa {listaDeTarefas[posicao_id].getTitle()} será concluida!")
        else:
            erroMensagem("Tarefa não encontrada.")
            return
    
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
                sucessoMensagem(f"A tarefa {listaDeTarefas[posicao_id].id}, descricao: {listaDeTarefas[posicao_id].desc} foi concluída")
            else:
                erroMensagem("Tarefa não encontrada.")
        else:
            avisoMensagem("Alteração não efetuada")
   
def exclui_tarefas(listaDeTarefas):

    if aListaTaVazia(listaDeTarefas):
        erroMensagem("Não há tarefas adicionadas.")
    else:
        linhaDivisoria()
        identificador = input("Identificador da tarefa(s): ")
    
        posicao_id =  localizaIndentificador(listaDeTarefas, identificador)

        if posicao_id == None:
            erroMensagem("Tarefa não encontrada.")
            return

        #mensagem aviso sobre exclusao de tarefa
        avisoMensagem(f"A tarefa {listaDeTarefas[posicao_id].getTitle()} não poderá ser recuperada após a remoção")
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
                sucessoMensagem("Tarefa removida com sucesso")
            else:
                erroMensagem("Tarefa não encontrada")
        else:
            avisoMensagem("Exclusão não efetuada")
   
def menu_principal():
    listaDeTarefas = []
    while True:
        tituloMensagem("\n*** Sistema de Gerenciamento de Tarefas ***")
        print("\t[0] - Sair")
        print("\t[1] - Adicionar tarefa")
        print("\t[2] - Visualizar tarefas")
        print("\t[3] - Atualizar tarefas")
        print("\t[4] - Concluir tarefas")
        print("\t[5] - Excluir tarefas")
        
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
            erroMensagem("Opção inválida!")
menu_principal()