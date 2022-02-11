class UFF: #Union-find forest
    def __init__(self, val, parent, rank):
        self.val=val
        self.parent=parent
        self.rank=rank

def make_set(v):
    v.parent=v
    v.rank=0

def find(v):
    if v.parent==v:
        return v
    else:
        v.parent=find(v.parent)
        return v.parent
    
def union(v, u):
    v=find(v)
    u=find(u)
    if v==u:
        return False
    if v.rank>u.rank:
        u.parent=v
    else:
        v.parent=u
        if v.rank==u.rank:
            u.rank+=1
    return True
    
def Kruskal(T):
    Vertices=[UFF(T[i], None, 0) for i in range(len(T))]
    Edges=[]
    for i in range(len(T)):
        Vertices[i].parent=Vertices[i]
        for j in range(i, len(T)):
            if T[i][j]!=-1:
                Edges.append((T[i][j], i, j))
    Edges=sorted(Edges)
    top=0
    suma=0
    print(Edges)
    while top!=len(Edges):
        k, v, u = Edges[top]
        print(k, v, u, suma)
        if union(Vertices[v], Vertices[u]) is True:
            suma+=k 
        top+=1
    return suma

G=[
    [-1, 2,-1,-1, 1],
    [ 2,-1, 4, 1,-1],
    [-1, 4,-1, 5,-1],
    [-1, 1, 5,-1, 3],
    [ 1,-1,-1, 3,-1]
]

print(Kruskal(G))