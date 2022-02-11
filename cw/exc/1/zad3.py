#Szymon Żychowicz
'''
algorytm opiera się na algorytmie Dijkstry
preprocessing: wyznaczam tablicę z nowymi optymalnymi krawędziami powstałymi przez ruch dwumilowymi butami (zmodyfikowany Floyd-Warshall)
działanie: wykonuję algorytm Dijkstry zapamiętując w jaki sposób przyszedłem na dane pole
złożoność: O(v^3)
'''
from zad3testy import runtests
from queue import PriorityQueue
from math import inf

class PQ:
    def __init__(self, dist, id, last):
        self.dist=dist
        self.id=id
        self.last=last
    def __gt__(self, other):
        return self.dist>other.dist
    def __ge__(self, other):
        return self.dist>=other.dist
    def __eq__(self, other):
        return self.dist==other.dist
    def __le__(self, other):
        return self.dist<=other.dis
    def __lt__(self, other):
        return self.dist<other.dist

def jumper(G, s, w):
    D = [ [ G[i][j] for j in range(len(G)) ] for i in range(len(G)) ]
    for i in range(len(G)):
        for j in range(len(G)):
            for t in range(len(G)):
                if G[i][t]!=0 and G[t][j]!=0 and i!=j and i!=t and t!=j:
                    if G[i][j]!=0:
                        if D[i][j]!=0:
                            D[i][j]=min(max(G[i][t], G[t][j]), G[i][j], D[i][j])
                        else:
                            D[i][j]=min(max(G[i][t], G[t][j]), G[i][j])
                    else:
                        if D[i][j]!=0:
                            D[i][j]=min(max(G[i][t], G[t][j]), D[i][j])
                        else:
                            D[i][j]=max(G[i][t], G[t][j])
    Proc=[[False, False] for _ in range(len(G))]
    Dist=[[inf, inf] for _ in range(len(G))]
    Dist[s][0]=0
    pq=PriorityQueue(len(G)**3)
    pq.put(PQ(0, s, 0))
    while pq.empty() is False:
        if Proc[w][0] is True or Proc[w][1] is True:
            break
        el=pq.get()
        v, dist, last = el.id, el.dist, el.last
        if Proc[v][last] is False:
            for i in range(len(G)):
                if G[i][v]!=0 and Dist[i][0]>dist+G[v][i]:
                    Dist[i][0]=dist+G[v][i]
                    pq.put(PQ(Dist[i][0], i, 0))
                if last==0 and D[v][i]!=0 and Dist[i][1]>dist+D[v][i]:
                    Dist[i][1]=dist+D[v][i]
                    pq.put(PQ(Dist[i][1], i, 1))
        Proc[v][last]=True
    return min(Dist[w][0], Dist[w][1])

runtests(jumper)