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
'''
tablica krawedzi:
[[0, 3], [2, 4], [4, 3], [4, 2], [3, 4], [3, 0], [5, 1], [5, 0], [1, 5], [0, 5], [6, 1], [6, 0], [0, 6], [1, 6], [6, 4], [4, 6]]
macierz:
[[0, 0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0, 0], [0, 0, 1, 1, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 1, 0, 0]]
sasiedztwo:
[[3, 5, 6], [5, 6], [4], [4, 0], [3, 2, 6], [1, 0], [1, 0, 4]]
'''