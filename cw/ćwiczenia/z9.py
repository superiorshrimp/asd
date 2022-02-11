'''
from queue import Queue

class Vertex:
    def __init__(self, p, edges=[], visited=False):
        self.p=p
        self.edges=edges
        self.visited=visited

def f(start, stop, level, diff, size):
    q=Queue(size)
    q.put(start)
    while q.qsize()!=0:
        v=q.get()
        for vertex in v.edges:
            if vertex.visited is False and abs(level-vertex.p)<=diff:
                vertex.visited=True
                q.put(vertex)
                if vertex==stop:
                    return True
    return False

P=[1, 3, 7, 5, 3, 4, 2]
T=[Vertex(P[i]) for i in range(len(P))]
tab=[[3, 5, 6], [5, 6], [4], [4, 0], [3, 2, 6], [1, 0], [1, 0, 4]]
for i in range(len(tab)):
    for j in range(len(tab[i])):
        T[i].edges.append(T[tab[i][j]])
print(f(T[0], T[4], T[0].p, 3, len(P)))
'''
'''
import queue

class Vertex:
    def __init__(self, color, edges):
        self.color=color
        self.edges=edges

def dwudzielnosc(vertex, size):
    q=queue.LifoQueue(size**2)
    q.put((vertex, -1))
    while q.empty() is False:
        v, last = q.get()
        if v.color is None:
            v.color=last*(-1)
            for vertex in v.edges:
                if vertex.color is None:
                    q.put((vertex, v.color))
        elif v.color!=(-1)*last:
            return False
    return True

size=7
T=[Vertex(None, []) for _ in range(size)]
tab=[[0, 3], [2, 4], [4, 3], [4, 2], [3, 4], [3, 0], [5, 1], [5, 0], [1, 5], [0, 5], [6, 1], [6, 0], [0, 6], [1, 6], [6, 4], [4, 6], [0,1], [1,0]]
for el in tab:
    T[el[0]].edges.append(T[el[1]])

print(dwudzielnosc(T[0], size))
tablica krawedzi:
[[0, 3], [2, 4], [4, 3], [4, 2], [3, 4], [3, 0], [5, 1], [5, 0], [1, 5], [0, 5], [6, 1], [6, 0], [0, 6], [1, 6], [6, 4], [4, 6]]
macierz:
[[0, 0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0, 0], [0, 0, 1, 1, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 1, 0, 0]]
sasiedztwo:
[[3, 5, 6], [5, 6], [4], [4, 0], [3, 2, 6], [1, 0], [1, 0, 4]]
'''