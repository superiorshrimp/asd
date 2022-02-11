class Vertex:
    def __init__(self, val, edges, parent): #val=-1 <==> visited=False
        self.val=val
        self.edges=edges
        self.parent=parent

class Global:
    def __init__(self, val):
        self.val=val

def DFS(v, time):
    low=v.val
    for edge in v.edges:
        if edge.val!=-1:
            if v.parent!=edge:
                low=min(low, edge.val)
        else:
            edge.parent=v
            edge.val=time.val
            time.val+=1
            DFS(edge, time)
            low=min(low, edge.val)
    v.val=low
    return

def f(V):
    time=Global(0)
    v=V[0]
    low=time.val
    time.val+=1
    v.val=low
    for edge in v.edges:
        if edge.val==-1:
            edge.val=time.val
            time.val+=1
            edge.parent=v
            DFS(edge, time)
    for i in range(len(V)):
        if V[i].val==i and V[i].parent!=None:
            print(i)

T=[
    [1,2],
    [0,2,3,4,6],
    [0,1],
    [1,5],
    [1,5],
    [3,4],
    [1]
]

V=[Vertex(-1, [], None) for i in range(len(T))]
for i in range(len(T)):
    for el in T[i]:
        V[i].edges.append(V[el])

f(V)