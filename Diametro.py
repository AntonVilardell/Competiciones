'''
Determinar el diàmetre d'un arbre

ALGORITME BFS (Breadth First Search - Cerca per Amplada)

Visitar tots els nodes del graf que hi ha en profunditat i abans de passar a visitar els
nodes de profunditat i+1
Desprès de visitar un node, visitem els seus germans abans que els seus fills.

In:
t   --> Nombre de grafos
n1  --> Indica que hi ha n-1 branques en l'arbre
x y --> Aresta de X a Y
x y
n2
x y
x y
'''
from collections import deque

if __name__ == '__main__':
    t = int(input())
    distancias = []
    distancias2 = []
    for i in range(t):
        d = int(input())
        grafo = [[] for i in range(d)]
        for m in range(d - 1):
            line = input().split()
            x = int(line[0])
            y = int(line[1])
            grafo[x].append(y)
            grafo[y].append(x)
            '''En la llista grafo incorporem a la posició corresponen els nodes conectats.'''
            '''[[4], [2,3] --> Node 0 connectat amb el node 4, Node 1 conectat amb el Node 2 i 3'''

        # Trobem el node de major profunditat usant BFS
        q = deque() #Cua
        visited = [False for i in range(d)] #LListat amb els nodes que visitem
        q.append((0,0)) #Ens posicionem en el Node 0 amb distància 0
        dist = 0
        visited[0] = True
        furthest = 0 #Ens determinarà el Node més llunyà
        while len(q) > 0:
            x, dist = q.popleft()
            fursthest = x
            for u in grafo[x]:
                if visited[u] == False:
                    visited[u] = True
                    q.append((u, dist+1))
                ''' Si els veíns del node on estem no han estat visitats, els incorporem a la cua i
                    augmentem distància.'''
        distancias.append(dist)

        # Trobem el diàmetre de l'arbre usant BFS
        q = deque()
        visited = [False for i in range(d)]
        q.append((fursthest, 0))    #Ens posicionem en el node més llunyà que hem trobat amb anterioritat usant BFS
        dist2 = 0
        visited[fursthest] = True
        furthest = 0
        while len(q) > 0:
            x, dist2 = q.popleft()
            for u in grafo[x]:
                if visited[u] == False:
                    visited[u] = True
                    q.append((u, dist2 + 1))

        distancias2.append(dist2)

for m in range(len(distancias2)):
    print(distancias2[m])