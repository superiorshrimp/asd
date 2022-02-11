class Pokemon:
    def __init__(self, free, edges, id):
        self.free=free
        self.edges=edges
        self.id=id

class Hauting_List:
    def __init__(self, predator, prey, next):
        self.predator=predator
        self.prey=prey
        self.next=next

def DFS(v, R):
    licznik=0
    for vtx in v.edges:
        if vtx.free is True:
            licznik+=1
        else:
            licznik+=DFS(vtx, R)
    if licznik>=2:
        v.free=True
        R.append(v.id)
        return 1
    else:
        print("0!!!!!!")
        return 0 #TODO: całość False

def RTA(HL, n):
    V=[Pokemon(False, [], i) for i in range(n)]
    P=[0 for _ in range(n)]
    R=[]
    while HL is not None:
        P[HL.predator]=1
        V[HL.predator].edges.append(V[HL.prey])
        HL=HL.next
    for i in range(len(P)):
        if P[i]==0:
            V[i].free=True
            R.append(i)
    for i in range(len(P)):
        if V[i].free is False:
            if DFS(V[i], R)==0:
                return False
    return R

T=[(0,1), (0,7), (0,3), (1,3), (1,7), (1,2), (4,5), (4,0), (6,2), (6,3)]
if len(T)==0:
    print("False")
    exit(0)
HL=Hauting_List(T[0][0], T[0][1], None)
head=HL
maksimum=0
for i in range(1, len(T)):
    maksimum=max(T[i][0], T[i][1], maksimum)
    HL.next=Hauting_List(T[i][0], T[i][1], None)
    HL=HL.next
print(RTA(head, maksimum+1))    
