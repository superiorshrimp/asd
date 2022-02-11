#nieskonczone ale nie mam sily

class Global:
    def __init__(self, val):
        self.val=val

class Vertex:
    def __init__(self, id, Edges, visited):
        self.id=id
        self.Edges=Edges
        self.visited=visited

def topological_sort(v, W, top):
    for edge in v.Edges:
        if edge.visited is False:
            edge.visited=True
            topological_sort(edge, W, top)
    W[top.val]=v.id
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

def nadgorliwy_mag(M) -> list:
    Res=silnie_spojne_skladowe(M)
    SSS=[None for _ in range(len(M))]
    for i in range(len(Res)):
        for el in Res[i]:
            SSS[el]=i
    G=[[0 for j in range(len(Res))] for i in range(len(Res))]
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j]==1 and SSS[i]!=SSS[j]:
                G[SSS[i]][SSS[j]]=1
    W=f(G)
    R=[None for _ in range(len(M))]
    p=0
    for el in W:
        for i in range(len(SSS)):
            if SSS[i]==el: 
                R[p]=i
                p+=1
    
    return R


G_1 = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]

G_2 = [[0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0]]

G_3 = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]


odp_1 = 3
odp_2 = 2
odp_3 = 4






































































































def valid_cycle(G, cycle):
    if len(cycle) == 1:
        return True
    i, j = 0, 1
    n = len(cycle)
    while j < n:
        if G[cycle[i]][cycle[j]] == 0:
            return False
        i += 1
        j += 1
    return True


def check_solution(G, solution, correct):
    if solution == None:
        return 2
    n = len(solution)
    i = 0
    counter = 0
    while i < n:
        first = solution[i]
        cycle = [first]
        temp = i
        i += 1
        while i < n and solution[i] != first:
            cycle.append(solution[i])
            i += 1
        if i == n and temp != n-1:
            return 2
        if not valid_cycle(G, cycle):
            return 3
        if i == n - 1:
            return True
        if i < n and G[first][solution[i + 1]] == 0:
            return 4
        i += 1
        counter += 1
    if counter != correct:
        return 5
    return True


if __name__ == "__main__":
    test = [(G_1, odp_1), (G_2, odp_2), (G_3, odp_3)]
    problem = False
    for i in range(len(test)):
        result = check_solution(test[i][0], nadgorliwy_mag(test[i][0]), test[i][1])
        if result == 2:
            print("Test", i + 1, ": nieprawidłowa odpowiedź.")
            problem = True
        elif result == 3:
            print("Test", i + 1, ": prawdopodobnie błędne przypisanie wież do jednego rytuału.")
            problem = True
        elif result == 4:
            print("Test", i + 1, ": próba przejścia pomiędzy wieżami nieistniejącym teleportem.")
            problem = True
        elif result == 5:
            print("Test", i + 1, ": niewłaściwa liczba rytuałów.")
            problem = True
        else:
            print("Test", i + 1, "ok.")
    if not problem:
        print("Wszystko ok <3")