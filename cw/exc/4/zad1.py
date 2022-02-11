#instrukcje niejasne

from math import sqrt, inf
from queue import PriorityQueue

class Vertex:
    def __init__(self, id, colour, Edges, Weights):
        self.id=id
        self.colour=colour
        self.Edges=Edges
        self.Weights=Weights

class PQ:
    def __init__(self, dist, v, clast, vlast, info):
        self.dist=dist
        self.v=v
        self.clast=clast
        self.vlast=vlast
        self.info=info
    def __gt__(self, other):
        return self.dist>other.dist
    def __ge__(self, other):
        return self.dist>=other.dist
    def __eq__(self, other):
        return self.dist==other.dist
    def __le__(self, other):
        return self.dist<=other.dist
    def __lt__(self, other):
        return self.dist<other.dist

def colour(val):
    if val=="BLOND":
        return 0
    return 1

def is_prime(n):
    if n==0:
        return True
    if n<2:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

def babiarz(G,T,W): #skoro nie wchodzi do pokojów mężczyzn to nie tworzę z nich wierzchołków
    V=[None for _ in range(len(G))]
    for i in range(len(G)):
        if is_prime(i) is True:
            V[i]=Vertex(i, colour(T[i]), [], [])
        else:
            V[i]=Vertex(-1, -1, [], [])
    for i in range(len(G)):
        if is_prime(i) is True:
            for j in range(len(G[i])):
                if is_prime(j) is True:
                    V[i].Edges.append(V[G[i][j][0]])
                    V[i].Weights.append(G[i][j][1])
    Dist=[[[inf for _ in range(len(V[i].Edges))] for j in range(2) ] for i in range(len(G))]
    Dist[0]=[[0 for _ in range(len(V[i].Edges))] for j in range(2) ]
    Proc=[[[False for _ in range(len(V[i].Edges))] for j in range(2) ] for i in range(len(G))]
    pq=PriorityQueue(2*len(G)**3)
    pq.put(PQ(0, V[0], 0, inf, 0))
    pq.put(PQ(0, V[0], 1, inf, 0))
    while pq.empty() is False:
        el=pq.get()
        dist, v, clast, vlast, info = el.dist, el.v, el.clast, el.vlast, el.info
        if dist>W:
            print(Dist)
            return
        if v.id==0 or (dist<W and Proc[v.id][clast][info]==False):
            i=0
            for k in range(len(v.Edges)):
                if v.Edges[i].id!=-1:
                    edge=v.Edges[i]
                    if edge.colour==clast and v.Weights[i]<vlast and Dist[edge.id][abs(clast-1)][i]>v.Weights[i]+dist:
                        Dist[edge.id][abs(clast-1)][i]=v.Weights[i]+dist
                        pq.put(PQ(v.Weights[i]+dist, edge, abs(clast-1), v.Weights[i], i))
                    i+=1
        if v.id!=0:
            Proc[v.id][clast][info]=True
    return 


G1 = [[(1,1),(2,5),(3,11),(4,3)],[(0,1),(3,3),(5,1),(6,1)],[(0,5),(3,3),(5,42)],[(2,3),(1,1),(0,11)],[(0,3)],[(2,42),(1,1)],[(1,1)]]
T1 = ["Łysy","Brun","Brun","Blond","Blond","Blond","Blond"]
W1 = 47
odp1 = [0,3,2]

G2 = [[(11,21),(8,15),(1,1),(2,5),(3,11),(4,3)],[(0,1),(3,3),(5,1),(6,1)],[(0,5),(3,3),(5,42)],[(2,3),(1,1),(0,11)],[(0,3)],[(2,42),(1,1)],[(1,1)],[(4,1),(8,10),(5,5)],[(0,15),(7,10)],[],[],[(0,21),(7,37)]]
T2 = ["Łysy","Brun","Blond","Brun","Blond","Blond","Brun","Blond","Blond","Brun","Brun","Blond"]
W2 = 63
odp2 = [0,11,7,5]

print(babiarz(G1,T1,W1) == odp1)
print(babiarz(G2,T2,W2) == odp2)
