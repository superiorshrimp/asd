class Vertex:
    def __init__(self, id, Edges, visited):
        self.id=id
        self.Edges=Edges
        self.visited=visited

class Global:
    def __init__(self, val):
        self.val=val

def topological_sort(v, W, top): #zał: brak cyklu ofc
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
    for el in W:
        print(el.id, end=' ')

G=[
    [0,1,0,0,1],
    [0,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,0],
    [0,0,0,0,0]
]
f(G)