class Vertex:
    def __init__(self, id, Edges, visited, nonexistent):
        self.id=id
        self.Edges=Edges
        self.visited=visited
        self.nonexistent=nonexistent

class Global:
    def __init__(self, val):
        self.val=val

def topological_sort(v, W, top): #zał: brak cyklu ofc
    for edge in v.Edges:
        if edge.visited is False:
            edge.visited=True
            topological_sort(edge, W, top)
    W[top.val]=v.id
    top.val+=1

def f(G):
    V=[Vertex(i, [], False, False) for i in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j]!=0:
                V[i].Edges.append(V[j])
        if len(V[i].Edges)==0:
            V[i].nonexistent=True
    top=Global(0)
    W=[None for _ in range(len(G))]
    for v in V:
        if v.visited is False and v.nonexistent is False:
            v.visited=True
            topological_sort(v, W, top)
    return W

def pijany_mag(T):
    M=[[0 for j in range(ord("z")-ord("a"))] for i in range(ord("z")-ord("a"))]
    Edges=[]
    for i in range(len(T)):
        for j in range(len(T)):
            p=0
            while p<min(len(T[i])-1, len(T[j])) and T[i][p]==T[j][p]:
                p+=1
            if i<j:
                Edges.append((ord(T[i][p])-ord("a")-1, ord(T[j][p])-ord("a")-1))
                M[ord(T[i][p])-ord("a")-1][ord(T[j][p])-ord("a")-1]=1
            elif i>j:
                Edges.append((ord(T[j][p])-ord("a")-1, ord(T[i][p])-ord("a")-1))
                M[ord(T[j][p])-ord("a")-1][ord(T[i][p])-ord("a")-1]=1
    W=f(M)
    I=[None for _ in range(len(M))]
    w=""
    i=0
    while i<len(W) and W[i] is not None:
        I[W[i]]=i
        w+=chr(W[i]+ord("a")+1)
        i+=1
    for edge in Edges:
        if I[edge[0]]<I[edge[1]]:
            return ""
    return w[::-1]
    










T1= ["wrt","wrf","er","ett","rftt"]
odp1 = 'wertf'

T2 = ['z','x']
odp2 = 'zx'

T3 = ['z','x','z']
odp3 = ''

tests = [(T1,odp1),(T2,odp2),(T3,odp3)]
for ind,(t,odp) in enumerate(tests):
    print('---------')
    print("test nr",ind)
    print("odpowiedz:",odp)
    a = pijany_mag(t)
    if a != odp:
        print(f"twoja odpowiedz: \"%s\"" % a)
        print("Błd w tescie")
    else:
        print("OK")