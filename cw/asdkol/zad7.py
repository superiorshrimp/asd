#Szymon Żychowicz
'''
algorytm najpierw wyznacza tablicę odległości między dowolnymi 2 wierzchołkami
a potem wykonuje udzwiniony algorytm Dijkstry próbując przejść zgodnie z warunkami zadania
odleglosci dist1 i dist2 okazaly sie nie potrzebne ale brak czasu na usuniecie
'''

from zad1testy import runtests
from queue import PriorityQueue

class Vertex:
    def __init__(self, id, Edges):
        self.id=id
        self.Edges=Edges

class PQ:
    def __init__(self, dist1, dist2, loc1, loc2, prev1, prev2):
        self.dist1=dist1
        self.dist2=dist2
        self.loc1=loc1
        self.loc2=loc2
        self.prev1=prev1
        self.prev2=prev2
    def __gt__(self, other):
        return self.dist1+self.dist2>other.dist1+other.dist2
    def __ge__(self, other):
        return self.dist1+self.dist2>=other.dist1+other.dist2
    def __eq__(self, other):
        return self.dist1+self.dist2==other.dist1+other.dist2
    def __lt__(self, other):
        return self.dist1+self.dist2<other.dist1+other.dist2
    def __le__(self, other):
        return self.dist1+self.dist2<=other.dist1+other.dist2

def keep_distance(M, x, y, d):
    D=[[M[i][j] for j in range(len(M))] for i in range(len(M))]
    V=[Vertex(i, []) for i in range(len(M))]
    suma=0
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j]!=0:
                V[i].Edges.append(V[j])
                if i<j:
                    suma+=M[i][j]

    for t in range(len(M)):
        for v in range(len(M)):
            for u in range(len(M)):
                if D[v][t]!=0 and D[t][u]!=0:
                    if D[v][u]==0:
                        if v!=u:
                            D[v][u]=D[v][t]+D[t][u]
                            D[u][v]=D[v][u]
                    else:
                        D[v][u]=min(D[v][u], D[v][t]+D[t][u])
                        D[u][v]=D[v][u]
    
    pq=PriorityQueue(suma*len(M)**2)
    new=PQ(0,0,x,y,x,y)
    pq.put(new)
    Prev=[[None for j in range(len(M))] for i in range(len(M))]
    Proc=[[False for j in range(len(M))] for i in range(len(M))]
    while pq.empty() is False:
        el=pq.get()
        dist1, dist2, loc1, loc2, prev1, prev2 = el.dist1, el.dist2, el.loc1, el.loc2, el.prev1, el.prev2
        if Proc[loc1][loc2] is False:
            Prev[loc1][loc2]=(prev1, prev2)
            if loc1==y and loc2==x:
                break
            for edge in V[loc1].Edges:
                if D[loc2][edge.id]>=d:
                    pq.put(PQ(dist1+M[loc1][edge.id], dist2, edge.id, loc2, loc1, loc2))
                for e in V[loc2].Edges:
                    if D[e.id][edge.id]>=d and (loc1!=e.id or loc2!=edge.id): #zmiana 1: dodany warunek if
                        pq.put(PQ(dist1+M[loc1][edge.id], dist2+M[loc2][e.id], edge.id, e.id, loc1, loc2))
            for edge in V[loc2].Edges:
                if D[loc1][edge.id]>=d:
                    pq.put(PQ(dist1, dist2+M[loc2][edge.id], loc1, edge.id, loc1, loc2))
        Proc[loc1][loc2]=True
    W=[(y,x)]
    loc1=y
    loc2=x
    while loc1!=x or loc2!=y: #zmiana 2: zmieniony warunek while
        W.append(Prev[loc1][loc2])
        loc1, loc2 = Prev[loc1][loc2]
    W.append((x,y))
    return W[::-1]

runtests( keep_distance )