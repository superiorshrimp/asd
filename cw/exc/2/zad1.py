from zad1testy import runtests
from queue import Queue

def furthest(v, size, G):
    Dist=[None for _ in range(size)]
    Dist[v]=0
    Q=Queue(size)
    Q.put(v)
    last=v
    while Q.empty() is False:
        v=Q.get()
        for edge in G[v]:
            if Dist[edge] is None:
                Dist[edge]=1+Dist[v]
                Q.put(edge)
                last=edge
    return last, Dist

def best_root( L ):
    v, _ = furthest(0, len(L), L)
    u, Dist = furthest(v, len(L), L)
    szukane=Dist[u]//2
    index=-1
    for i in range(len(Dist)):
        if Dist[i]==szukane:
            index=i
            break
    return index


runtests( best_root ) 
