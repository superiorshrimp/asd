'''
algorytm zczytując dane z tablicy G zapamiętuje krawędzie. potem usuwa (wirtualnie; tak na prawdę nic nie usuwa) każdą po kolei w pętli (po przetworzeniu odnawiając każdą).
po usunięciu krawędzi korzystając z algorytmu Dijkstry szuka najkrótszej ścieżki między wierzchołkami krawędzi usuniętej w danym przebiegu.
jeśli ta najkrótsza ścieżka + odległość tych punktów jest minimalna to znaleźliśmy najkrótszy cykl (najkrótsza taka ścieżka + usunięta krawędź stanowi cykl).
z pliku wzorcowego można się dowiedzieć, że wiemy, że sprawdzany graf ma cykl eulera więc zawsze nie dość, że jest spójny (nie wywali mi się warunek while w funkcji Dijkstra) to każdy wierzchołek należy do jakiegoś cyklu
złożoność: O(V^2+E*E*logV) czyli O(E^2*logV) 
'''

from math import inf
from queue import PriorityQueue

class Vertex: #klasa opisująca wierzchołek
    def __init__(self, id, edges, dist, prev, pid, vid):
        self.id=id #oznaczenie numeryczne obiektu
        self.edges=edges #krawędzie wychodzące z wierzchołka
        self.dist=dist #najkrótsza długość ścieżki do wierzchołka
        self.prev=prev #w zasadzie parent z wykładu
        self.pid=pid #czy przetworzono wierzchołek w odpowiednim przebiegu; processed id
        self.vid=vid #czy odwiedzono wierzchołek w odpowiednim przebiegu; visited id
    #poniższe linijki służą do tego, aby PriorityQueue mogła porównywać wierzchołki
    def __gt__(self, other):
        return self.dist>other.dist
    def __ge__(self, other):
        return self.dist>=other.dist
    def __eq__(self, other):
        return self.dist==other.dist
    def __lt__(self, other):
        return self.dist<other.dist
    def __le__(self, other):
        return self.dist<=other.dist

def min_cycle(T):
    Vertices=[Vertex(i, [], inf, None, -1, -1) for i in range(len(T))] #tworzę wierzchołki
    Edges=[] #tworzę tablicę, która zapisze istniejące krawędzie
    for row in range(len(T)): #zczytuję dane z tablicy T
        for col in range(len(T)):
            if T[row][col]!=-1: #istnieje krawędź między row a col
                Vertices[row].edges.append(Vertices[col])
                if row<col:
                    Edges.append((row, col))
    shortest=inf #długość najkrótszego cyklu
    for i in range(len(Edges)): #dla każdej krawędzi w grafie
        s, t = Edges[i] #zczytuję jej początek i koniec
        q=Dijkstra(s, t, Vertices, T, i)+T[s][t]  #wykonuję algorytm Dijkstry na grafie bez jednej krawędzi (to że bez jednej krawędzi jest rozpatrywane wewnątrz funkcji) i dodaję jej odległość (powstaje długość cyklu)
        if q<shortest: #jeśli jest najkrótszy ten cykl to zapamiętuję jego długość i jego samego
            W=[]
            shortest=q
            v=Vertices[t]
            W.append(v.id)
            while v.prev is not None:
                v=v.prev
                W.append(v.id)
    return W

def Dijkstra(s, t, Vertices, Distances, i):
    min_heap=PriorityQueue(len(Distances)**2)
    v=Vertices[s]
    v.dist=0
    v.vid=i
    min_heap.put(v) #odkładam na PriorityQueue wierzchołek s
    v.prev=None
    while Vertices[t].pid!=i: #while docelowa krawędź (t) nie była w przebiegu i przetworzona
        v=min_heap.get()
        if v.pid!=i: #jeśli ściągnięty z PriorityQueue wierzchołek nie był przetworzony w tym przebiegu
            for j in range(len(v.edges)): #dla każdej jego krawędzi 
                u=v.edges[j]
                if (u.id==s and v.id==t) or (u.id==t and v.id==s) is False: #jeśli nie jest to usunięta krawędź
                    if u.vid==i: #jeśli wierzchołek na końcu sprawdzanej krawędzi był odwiedzony (w przebiegu i) to sprawdzam czy da się do niego dotrzeć szybciej
                        if Distances[v.id][u.id]+v.dist<u.dist:
                            u.dist=Distances[v.id][u.id]+v.dist
                            min_heap.put(u)
                            u.prev=v
                    else: #jeśli nie to szacuję jego odległość
                        u.vid=i
                        u.dist=Distances[v.id][u.id]+v.dist
                        min_heap.put(u)
                        u.prev=v
            v.pid=i #przetworzyłem wierzchołek zdjęty z kolejki prio. (nie da się do niego dotrzeć szybciej [z zasady działania algorytmu Dijkstry])
    return Vertices[t].dist
  
### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera)
### funkcja zwraca prawidłowy wynik
  
G = [
[-1, 0, -1, -1],
[0, -1, 3, 2], 
[-1, 3, -1, 1], 
[-1, 2, 1, -1]
]

print(min_cycle(G))

class UFF: #Union-find forest
    def __init__(self, val, parent, rank):
        self.val=val
        self.parent=parent
        self.rank=rank

def make_set(v):
    v.parent=v
    v.rank=0

def find(v):
    if v.parent==v:
        return v
    else:
        v.parent=find(v.parent)
        return v.parent
    
def union(v, u):
    v=find(v)
    u=find(u)
    if v==u:
        return False
    if v.rank>u.rank:
        u.parent=v
    else:
        v.parent=u
        if v.rank==u.rank:
            u.rank+=1
    return True
    
def Kruskal(T):
    Vertices=[UFF(T[i], None, 0) for i in range(len(T))]
    Edges=[]
    for i in range(len(T)):
        Vertices[i].parent=Vertices[i]
        for j in range(i, len(T)):
            if T[i][j]!=-1:
                Edges.append((T[i][j], i, j))
    Edges=sorted(Edges)
    top=0
    suma=0
    print(Edges)
    while top!=len(Edges):
        k, v, u = Edges[top]
        print(k, v, u, suma)
        if union(Vertices[v], Vertices[u]) is True:
            suma+=k 
        top+=1
    return suma

G=[
    [-1, 2,-1,-1, 1],
    [ 2,-1, 4, 1,-1],
    [-1, 4,-1, 5,-1],
    [-1, 1, 5,-1, 3],
    [ 1,-1,-1, 3,-1]
]

print(Kruskal(G))


'''
algorytm zczytując dane z tablicy G zapamiętuje krawędzie. potem usuwa każdą po kolei w pętli (po przetworzeniu odnawiając każdą).
po usunięciu krawędzi korzystając z algorytmu Dijkstry szuka najkrótszej ścieżki między wierzchołkami krawędzi usuniętej w danym przebiegu.
jeśli ta najkrótsza ścieżka + odległość tych punktów jest minimalna to znaleźliśmy najkrótszy cykl (najkrótsza taka ścieżka + usunięta krawędź stanowi cykl).

'''

from math import inf
from queue import PriorityQueue
from copy import deepcopy

class Vertex: #klasa opisująca wierzchołek
    def __init__(self, id, edges, dist, prev, pid, vid):
        self.id=id #oznaczenie numeryczne obiektu
        self.edges=edges #krawędzie wychodzące z wierzchołka
        self.dist=dist #najkrótsza długość ścieżki do wierzchołka
        self.prev=prev #w zasadzie parent z wykładu
        self.pid=pid #czy przetworzono wierzchołek w odpowiednim przebiegu; processed id
        self.vid=vid #czy odwiedzono wierzchołek w odpowiednim przebiegu; visited id
    #poniższe linijki służą do tego, aby PriorityQueue mogła porównywać wierzchołki
    def __gt__(self, other):
        return self.dist>other.dist
    def __ge__(self, other):
        return self.dist>=other.dist
    def __eq__(self, other):
        return self.dist==other.dist
    def __lt__(self, other):
        return self.dist<other.dist
    def __le__(self, other):
        return self.dist<=other.dist

def min_cycle(T):
    Vertices=[Vertex(i, [], inf, None, -1, -1) for i in range(len(T))] #tworzę wierzchołki
    Edges=[] #tworzę tablicę, która zapisze istniejące krawędzie
    for row in range(len(T)): #zczytuję dane z tablicy T
        for col in range(len(T)):
            if T[row][col]!=-1: #istnieje krawędź między row a col
                Vertices[row].edges.append(Vertices[col])
                if row<col:
                    Edges.append((row, col))
    shortest=inf #długość najkrótszego cyklu
    for i in range(len(Edges)): #dla każdej krawędzi w grafie
        s, t = Edges[i] #zczytuję jej początek i koniec
        q=Dijkstra(s, t, Vertices, T, i)+T[s][t]  #wykonuję algorytm Dijkstry na grafie bez jednej krawędzi (to że bez jednej krawędzi jest rozpatrywane wewnątrz funkcji) i dodaję jej odległość (powstaje długość cyklu)
        if q<shortest: #jeśli jest najkrótszy ten cykl to zapamiętuję jego długość i jego samego
            W=[]
            shortest=q
            v=Vertices[t]
            W.append(v.id)
            while v.prev is not None:
                v=v.prev
                W.append(v.id)
    return W

def Dijkstra(s, t, Vertices, Distances, i):
    min_heap=PriorityQueue(len(Distances)**2)
    v=Vertices[s]
    v.dist=0
    v.vid=i
    min_heap.put(v) #odkładam na PriorityQueue wierzchołek s
    v.prev=None
    while Vertices[t].pid!=i: #while docelowa krawędź (t) nie była w przebiegu i przetworzona
        v=min_heap.get()
        if v.pid!=i: #jeśli ściągnięty z PriorityQueue wierzchołek nie był przetworzony w tym przebiegu
            for j in range(len(v.edges)): #dla każdej jego krawędzi 
                u=v.edges[j]
                if (u.id==s and v.id==t) or (u.id==t and v.id==s) is False: #jeśli nie jest to usunięta krawędź
                    if u.vid==i: #jeśli wierzchołek na końcu sprawdzanej krawędzi był odwiedzony (w przebiegu i) to sprawdzam czy da się do niego dotrzeć szybciej
                        if Distances[v.id][u.id]+v.dist<u.dist:
                            u.dist=Distances[v.id][u.id]+v.dist
                            min_heap.put(u)
                            u.prev=v
                    else: #jeśli nie to szacuję jego odległość
                        u.vid=i
                        u.dist=Distances[v.id][u.id]+v.dist
                        min_heap.put(u)
                        u.prev=v
            v.pid=i #przetworzyłem wierzchołek zdjęty z kolejki prio. (nie da się do niego dotrzeć szybciej [z zasady działania algorytmu Dijkstry])
    return Vertices[t].dist

G=[
    [-1, 2,-1,-1, 1],
    [ 2,-1, 4, 1,-1],
    [-1, 4,-1, 5,-1],
    [-1, 1, 5,-1, 3],
    [ 1,-1,-1, 3,-1]
]

print(min_cycle(G))

#start

from math import inf

class Vertex:
    def __init__(self, id, val, visited, edges):
        self.id=id
        self.val=val
        self.visited=visited
        self.edges=edges

def top_sort(v, R):
    v.visited=True
    for edge in v.edges:
        if edge.visited is False:
            top_sort(edge, R)
    R.append(v.id)

def f(T, s):
    Vertices=[Vertex(i, inf, False, []) for i in range(len(T))]
    for row in range(len(T)):
        for col in range(len(T)):
            if T[row][col]!=0:
                Vertices[row].edges.append(Vertices[col])
    R=[]
    for v in Vertices:
        if v.visited is False:
            top_sort(v, R)
    flag=0
    Vertices[R[len(R)-1]].val=0
    for i in range(len(R)-1,-1,-1):
        if R[i]==s:
            flag=1
        if flag==1:
            for edge in Vertices[R[i]].edges:
                edge.val=min(Vertices[R[i]].val+T[R[i]][edge.id], edge.val)
    print(Vertices[R[0]].val)
    
T=[
    [0,1,3,0,0],
    [0,0,1,0,8],
    [0,0,0,4,3],
    [0,0,0,0,1],
    [0,0,0,0,0]
]

f(T, 0)

#koniec

