from zad3testy import runtests

class Vertex:
    def __init__(self, id, Edges, visited):
        self.id=id
        self.Edges=Edges
        self.visited=visited

class Global:
    def __init__(self, val):
        self.val=val

def topological_sort(v, W, top):
    for edge in v.Edges:
        if edge.visited is False:
            edge.visited=True
            topological_sort(edge, W, top)
    W[top.val]=v
    top.val-=1

def f(G):
    V=[Vertex(i, [], False) for i in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j]!=0:
                V[i].Edges.append(V[j])
    top=Global(len(G)-1)
    W=[None for _ in range(len(G))]
    for v in V:
        if v.visited is False:
            v.visited=True
            topological_sort(v, W, top)
    return W

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

def tasks(T):
    M=[[1 if T[i][j]<2 and i!=j else 0 for j in range(len(T))] for i in range(len(T))]
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
    W=f(G)
    Return=[None for _ in range(len(T))]
    top=0
    for el in W:
        for v in Res[el.id]:
            Return[top]=v
            top+=1
    return Return

runtests( tasks )
