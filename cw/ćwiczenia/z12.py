def transitive_closure(T): #FLoyd Warshall prawie
    for t in range(len(T)):
        for v in range(len(T)):
            for u in range(len(T)):
                if T[v][t]+T[t][u]==2:
                    T[v][u]=1
    for row in T:
        print(row)

T=[
    [0,1,1,0,0,0],
    [0,0,1,1,1,0],
    [0,0,0,1,0,0],
    [0,0,0,0,0,1],
    [0,0,0,0,0,1],
    [0,0,0,0,0,0]
]
transitive_closure(T)

from math import inf
from queue import PriorityQueue

def f(T, s, t): #zmodyfikowany Dijkstra
    maksimum=0
    for i in range(len(T)):
        maksimum=max(maksimum, T[s][i])
    Value=[[0 if i==s else inf for j in range(maksimum+1)] for i in range(len(T))]    
    Q=PriorityQueue(len(T)**2)
    Q.put((s, inf, 0)) #parent, wartosc krawedzi do parent, suma do tego momentu najnizsza dla danej wartosci
    while Q.empty() is False:
        v, k, suma = Q.get()
        for i in range(len(T)):
            if 0<T[v][i]<k and Value[i][T[v][i]]>suma+T[v][i]:
                Q.put((i, T[v][i], suma+T[v][i]))
                Value[i][T[v][i]]=suma+T[v][i]
    minimum=inf
    for i in range(len(Value[t])):
        minimum=min(minimum, Value[t][i])
    return minimum
    
T=[
    [0,100,40,60,0,0,0,0],
    [100,0,0,0,0,0,80,0],
    [40,0,0,50,0,35,0,0],
    [60,0,50,0,10,29,0,0],
    [0,0,0,10,0,0,0,0],
    [0,0,35,29,0,0,10,30],
    [0,80,0,0,0,10,0,20],
    [0,0,0,0,0,30,20,0]
]

print(f(T, 0, len(T)-1))