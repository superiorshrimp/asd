from zad1testy import runtests

#Szymon Żychowicz
'''
algorytm tworzy DAG taki, że pozwala dynamicznie wybierać optymalne połączenia.
tworzy pożądek topologiczny i przechodząc od lewej po nim wypełnia kolejne pola v.f i edge.f
zapisuje przy tym skad przyszedl optymalny wynik
potem szuka maksymalnego wyniku spelniającego rozwiązanie i go wypisuje
przepraszam za taki niedokladny opis ale mam 2 min do wyslania
złożoność: O(E+V)
pamięciowa: O(V^2)
''' 
class Vertex:
    def __init__(self, profit, a, b, w, id, edges, f, prev):
        self.profit=profit
        self.a=a
        self.b=b
        self.w=w
        self.id=id
        self.edges=edges
        self.f=f
        self.prev=prev
    def __gt__(self, other):
        return self.b>other.b
    def __ge__(self, other):
        return self.b>=other.b
    def __eq__(self, other):
        return self.b==other.b
    def __lt__(self, other):
        return self.b<other.b
    def __le__(self, other):
        return self.b<=other.b

def top_order(v, R, Visited):
    global top
    if len(v.edges)==0:
        R[top]=v
        top-=1
        return
    for edge in v.edges:
        Visited[edge.id]=True
        top_order(edge, R, Visited)
    R[top]=v
    top-=1

def select_buildings(T, p):
    top=len(T)-1
    V=[Vertex(T[i][0]*(T[i][2]-T[i][1]), T[i][1], T[i][2], T[i][3], i, [], [[0 for _ in range(p+1)] for j in range(len(T))], [None for k in range(p+1)]) for i in range(len(T))]
    V=sorted(V)
    for v in V:
        flag=0
        for vtx in V:
            if vtx.a>v.b:
                if flag==0:
                    stop=vtx.b
                if vtx.a<=stop:
                    v.edges.append(vtx)
    R=[None for _ in range(len(T))]
    Visited=[False for _ in range(len(T))]
    for v in V:
        if Visited[v.id]==False:
            Visited[v.id]=True
            top_order(v, R, Visited)
    for v in R:
        v.f[v.id][v.w]=v.profit
    for v in R:
        for new_w in range(p, v.w+2, -1):
            for i in range(len(T)):
                if v.f[i][new_w-v.w]!=0:
                    v.f[v.id][new_w]=max(v.f[v.id][new_w], v.f[i][new_w-v.w]+v.profit)
        for edge in v.edges:
            for new_w in range(p, 1, -1):
                if edge.f[v.id][new_w]<v.f[v.id][new_w]:
                    edge.f[v.id][new_w]=v.f[v.id][new_w]
                    edge.prev[new_w]=v
    maksimum=0
    minimum=p+1
    best=None
    best_index=None
    for v in V:
        for i in range(len(v.f[v.id])):
            if maksimum<v.f[v.id][i]:
                maksimum=v.f[v.id][i]
                minimum=i
                best=v
                best_index=i
            elif maksimum==v.f[v.id][i] and i<minimum:
                maksimum=v.f[v.id][i]
                minimum=i
                best=v
                best_index=i
    Res=[best.id]
    for v in V:
        print()
    while best.prev[best_index] is not None:
        Res.append(best.prev[best_index].id)
    return Res


runtests(select_buildings)