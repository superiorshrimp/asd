from zad3_testy import run_tests
from math import inf

def Dijkstra(M, s, t):
    Dist=[inf for _ in range(len(M))]
    Dist[s]=0
    Proc=[False for _ in range(len(M))]
    procd=0
    Prev=[None for _ in range(len(M))]
    while procd<len(M):
        if Proc[t]==True:
            break
        min_id=-1
        minimum=inf
        for v in range(len(Dist)):
            if Dist[v]<minimum and Proc[v]==False:
                minimum=Dist[v]
                min_id=v
        v=min_id
        for u in range(len(M)):
            if v!=u and M[v][u]!=0 and Dist[u]>Dist[v]+M[v][u]:
                Prev[u]=v
                Dist[u]=Dist[v]+M[v][u]
        procd+=1
        Proc[v]=True
    Path=[]
    last=t
    while last is not None:
        Path.append(last)
        last=Prev[last]
    return Dist[t], Path

def gorszy_mag(G) -> list:
    Edges=[]
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j]!=0 and i<j:
                Edges.append((G[i][j], i, j))
    minimum=inf
    min_path=None   
    for edge in Edges:
        val, a, b = edge
        G[a][b]=0
        G[b][a]=0
        dist, path = Dijkstra(G, a, b)
        if dist+val<minimum:
            minimum=dist+val
            min_path=path
        G[a][b]=val
        G[b][a]=val
    if minimum==inf:
        minimum=None
    return minimum, min_path

run_tests(gorszy_mag)