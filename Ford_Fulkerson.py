from queue import Queue
from math import inf

def BFS(C, F, s, t):
    q=Queue(len(C)**2)
    Prev=[None for _ in range(len(C))] #pelni tez funkcje Visited
    Prev[s]=s
    q.put((s, inf))
    flow=inf
    while Prev[t] is None and q.empty() is False:
        v, flow = q.get()
        for i in range(len(C)):
            if Prev[i] is None and C[v][i]-F[v][i]>0:
                Prev[i]=v
                flow=min(flow, C[v][i]-F[v][i])
                q.put((i, flow))
    return Prev, flow

def Ford_Fulkerson(C, s, t):
    F=[[0 for j in range(len(C))] for i in range(len(C))]
    path, flow = BFS(C, F, s, t)
    while path[t] is not None:
        i=t
        while path[i]!=i:
            F[path[i]][i]+=flow
            F[i][path[i]]+=flow
            i=path[i]
        path, flow = BFS(C, F, s, t)
    suma=0
    for row in F:
        print(row)
    for i in range(len(C)):
        suma+=F[i][t]
    return suma

# make a capacity graph
# node   s   o   p   q   r   t
C = [[ 0, 3, 3, 0, 0, 0 ],  # s
     [ 0, 0, 2, 3, 0, 0 ],  # o
     [ 0, 0, 0, 0, 2, 0 ],  # p
     [ 0, 0, 0, 0, 4, 2 ],  # q
     [ 0, 0, 0, 0, 0, 2 ],  # r
     [ 0, 0, 0, 0, 0, 3 ]]  # t

source = 0  # A
sink = 5    # F
print(Ford_Fulkerson(C, source, sink))