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
    for i in range(len(M)):
        print(Dist[i])
    #return Dist[t]

G = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]]
print(Dijkstra(G, 0, 1))