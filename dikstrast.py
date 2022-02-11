from queue import Queue
from math import inf

from math import inf

def Dijkstra(M, s, t):
    Dist=[inf for _ in range(len(M))]
    Dist[s]=0
    Proc=[False for _ in range(len(M))]
    procd=0
    while procd<len(M):
        min_id=-1
        minimum=inf
        for v in range(len(Dist)):
            if Dist[v]<minimum and Proc[v]==False:
                minimum=Dist[v]
                min_id=v
        v=min_id
        for u in range(len(M)):
            if M[v][u]!=0 and Dist[u]>Dist[v]+M[v][u]:
                Dist[u]=Dist[v]+M[v][u]
        procd+=1
        Proc[v]=True
    print(Dist)
    #return Dist[t]

def f(G, s, t):
    Dist=[inf for _ in range(len(G))]
    Dist[s]=0
    q=Queue(len(G)**2)
    q.put((s, 0))
    while q.empty() is False:
        el=q.get()
        v=el[0]
        k=el[1]
        if k!=0:
            q.put((v, k-1))
        else:
            for i in range(len(G)):
                if G[v][i]!=0 and Dist[i]>Dist[v]+G[v][i]:
                    Dist[i]=Dist[v]+G[v][i]
                    q.put((i, G[v][i]-1))
    print(Dist)

G = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]]
Dijkstra(G, 0, 1)
f(G, 0, 1)