from operator import attrgetter
class Tarefa(object):
    def __init__(self,descricao,prioridade):
        self.descricao=descricao        
        self.prioridade=int (prioridade)
    
    def __str__(self):
        return "%s - %s" % (str(self.prioridade), str(self.descricao))
 
    
    def setTarefa(self,descricao,prioridade):
        self.descricao=descricao
        self.prioridade=prioridade

    
    def getPrioridade(self):
        return self.prioridade

    def getDescricao(self):
        return self.descricao
    
    def Imprimir(self):
        print(self.getPrioridade()+self.getDescricao)
    


vet=[]
for aux in range(10):
    a= input("digite a descricao da tarefa: ")
    b=int(input("digite o numero que corresponda a ordem de execução da tarefa: "))
    tarefa=Tarefa(a,b)
    tarefa.setTarefa(a,b)
    vet.append(tarefa)
 
prio=vet.sort(key=lambda a: a.prioridade)
print("ordem das tarefas:")
for aux in range(10):
    print (vet[aux].getDescricao())
