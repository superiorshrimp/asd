from math import inf

class Node:
    def __init__(self, val, next=None):
        self.val=val
        self.next=next

class Queue:
    def __init__(self):
        self.first=None
        self.last=None
        self.count=0
    def q_size(self):
        return self.count
    def get(self):
        if self.q_size()!=0:
            element=self.first
            self.first=element.next
            self.count-=1
            return element.val
    def put(self, new_value):
        new=Node(new_value)
        if self.q_size()!=0:
            element=self.last
            element.next=new
            self.last=new
            self.count+=1
        else:
            self.count=1
            self.first=new
            self.last=new

class Vertex:
    def __init__(self, edges, dists):
        self.edges=edges
        self.dists=dists

def BFS_k(v, n, k):
    minimum=inf
    q=Queue()
    v.dists[0]=0
    q.put((v, 1))
    while q.q_size()>0:
        v, level = q.get()
        for edge in v.edges:
            edge[0].dists[level]=min(edge[0].dists[level], v.dists[level-1]+edge[1])
            if level<k-1:
                q.put((edge[0], level+1))
            else:
                minimum=min(minimum, edge[0].dists[level])
    return minimum

def impatientBob(J, n, k):
    Vertices=[Vertex([], [inf for _ in range(k)]) for _ in range(len(J))]
    for i in range(len(J)):
        stop=inf
        for j in range(i+1, len(J)):
            if J[j][0]>=J[i][1]:
                stop=min(stop, j)
                if J[j][0]<J[stop][1]:
                    Vertices[i].edges.append((Vertices[j], J[j][0]-J[i][1]))
    minimum=inf
    for v in Vertices:
        minimum=min(minimum, BFS_k(v, n, k))
    return minimum

#J=[(0,6),(2,5), (7,9),(8,11),(7,11), (12,19),(13,20)]
J=[(0,3), (5,6),(7,8), (4, 10), (14,15)]
print(impatientBob(J, len(J)-1, 3))
    