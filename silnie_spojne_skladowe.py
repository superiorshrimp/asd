class Global:
    def __init__(self, val):
        self.val=val

def DFS_visit(T, v, Visited, Time, H, time):
    Visited[v]=True
    for i in range(len(T[v])):
        if T[v][i]==1 and Visited[i] is False:
            DFS_visit(T, i, Visited, Time, H, time)
    Time[v]=time.val
    H[time.val]=v
    time.val+=1

def DFS_visit_r(T, v, Visited, R):
    Visited[v]=True
    for i in range(len(T)):
        if T[i][v]==1 and Visited[i] is False:
            DFS_visit_r(T, i, Visited, R)
    R.append(v)

def silnie_spojne_skladowe(T): #T-macierz
    time=Global(0)
    Visited=[False for _ in range(len(T))]
    Time=[None for _ in range(len(T))]
    H=[None for _ in range(len(T))]
    for v in range(len(T)):
        if Visited[v] is False:
            DFS_visit(T, v, Visited, Time, H, time)
    Visited=[False for _ in range(len(T))]
    Res=[]
    for i in range(len(T)-1,-1,-1):
        R=[]
        if Visited[H[i]] is False:
            DFS_visit_r(T, H[i], Visited, R)
            Res.append(R)
    return Res

T=[
    [2,4],
    [0,9],
    [1],
    [4,6],
    [5],
    [3],
    [5],
    [3,9],
    [7],
    [10],
    [6,8],
]

M=[[1 if j in T[i] else 0 for j in range(len(T))] for i in range(len(T))]

Res=silnie_spojne_skladowe(M)
SSS=[None for _ in range(len(T))]
for i in range(len(Res)):
    for el in Res[i]:
        SSS[el]=i
G=[[0 for j in range(len(Res))] for i in range(len(Res))]
for i in range(len(M)):
    for j in range(len(M)):
        if T[i][j]==1 and SSS[i]!=SSS[j]:
            G[SSS[i]][SSS[j]]=1