from collections import defaultdict
 
# Essa classe representa um grafo direcionado
# Usando matriz adjacentes
class Grafo:
 
    def __init__(self, grafo):
        self.grafo = grafo  # grafo residual
        self.linha = len(grafo)
 
    '''Retorna true se tiver um caminho da fonte 's' para o sumidouro 't' no grafo residual. Também adiciona os antecessores[] para guardar o  caminho '''
 
    def BFS(self, s, t, antecessores):
 
        # Marcar todos os vértices como não visitado
        visitado = [False]*(self.linha)
 
        # Criar uma fila de prioridades "Q" para o BFS
        FilaQ = []
 
        # Marca o nó visitado e o adiciona na fila
        FilaQ.append(s)
        visitado[s] = True
 
        # Loop para o BFS
        while FilaQ:
            # Desenfilera um vértice da fila Q
            u = FilaQ.pop(0)
 
            # Pega todos os vértices adjacentes do vértice u
            # Se um vértice adjacente não foi visitado, então ele é marcado e o adicionado na fila
            for i, w in enumerate(self.grafo[u]):
                if visitado[i] == False and w > 0:

                    # Se for encontrado uma conexão com o nó sumidouro
                    # então não tem mais pontos no BFS, precisamos apenas ajustar os antecessores e retornar true
                    FilaQ.append(i)
                    visitado[i] = True
                    antecessores[i] = u
                    if i == t:
                        return True
 
        #Se não for encontrado o sumidouro através do sumidouro então retorna false 
        return False
             
    # Retorna o flow máximo do ponto "s" até "t"
    def FordFulkerson(self, fonte, sumidouro):
        # Esta matriz é preenchida pelo BFS e para armazenar o caminho
        antecessores = [-1]*(self.linha)
 
        # Fluxo inciado com valor 0
        fluxo_max = 0
 
        # Aumenta o fluxo enquanto houver caminho da fonte "s" até o sumidouro "t"
        while self.BFS(fonte, sumidouro, antecessores) :
 
            # Encontra o fluxo máximo através do caminho encontrado
            caminho = float("Inf")
            s = sumidouro
            while(s !=  fonte):
                caminho = min (caminho, self.grafo[antecessores[s]][s])
                s = antecessores[s]
 
            # Adiciona o fluxo do caminho ao fluxo geral
            fluxo_max += caminho
 
            # Atualiza as capacidades residuais das arestas e das arestas reversas ao longo do caminho
            v = sumidouro
            while(v !=  fonte):
                u = antecessores[v]
                self.grafo[u][v] -= caminho
                self.grafo[v][u] += caminho
                v = antecessores[v]
 
        return fluxo_max
    
    def printGrafo(self):
        #Mostrar o grafo
        print("Grafo:")
        for i in range(self.linha):
            print(self.grafo[i])
 
#Grafo de exemplo 
grafo = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10, 12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]
 
g = Grafo(grafo)
 
fonte = 0; 
sumidouro = 5

g.printGrafo()  
print ("O fluxo máximo possível é: %d " % g.FordFulkerson(fonte, sumidouro))
