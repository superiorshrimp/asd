from math import inf

def BellmanFord(Edges, n, s): #lista krawędzi, ilość wierzchołków, start
    Dist=[inf for  in range(n)]
    Dist[s]=0
    for i in range(n-1):
        for e in Edges:
            v, u, k = e
            Dist[u]=min(Dist[v]+k, Dist[u])
    for e in Edges:
        v, u, k = e
        if Dist[u]>Dist[v]+k:
            return []
    return Dist
#A-0 B-1 C-2 D-3 E-4
Edges=[
    (0,1,2),
    (0,2,4),
    (1,2,3),
    (1,3,3),
    (2,4,4),
    (2,3,-1),
    (3,4,2)
]
print(Bellman_Ford(Edges, 5, 0))