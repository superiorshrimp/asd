#Szymon Żychowicz
'''
Algorytm wykonuje BFS zapisując wierzchołki z których przyszliśmy w najkrótszej odległości.
Potem mając zapisane te właśnie wierzchołki wraca się po nich zapisując na ile wierzchołków było na danej odległości w optymalnym przebiegu.
Jeśli na dwóch odległościach obok siebie optymalna ścieżka przechodziła w obu po dokładnie jednym wierzchołku to krawędź między nimi jest szukana.
Złożoność: O(V+E)
pamięciowa: O(V+E)
'''
from zad2testy import runtests
class Node: #Node jest potrzebny do mojej kolejki
    def __init__(self, val, next=None):
        self.val=val
        self.next=next

class Queue: #zaimplementowałem wcześniej własną kolejkę, bo dzięki temu lepiej wiem jak działa niż z gotowych bibliotek
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

class Vertex: #łatwiej operuje mi się na wierzchołkach zapisanych jako obiekty
    def __init__(self, val, prev, edges, id):
        self.val=val #najkrótsza odległość od s
        self.prev=prev #skąd na nią przyszedłem; tablica
        self.edges=edges #do jakich wierzchołków prowadzą krawędzie
        self.id=id #numer wierzchołka jako liczba

def DFS(v, Visited, n, Dist): #2gie zdanie opisu algorytmu; 
    if len(v.prev)==0: #dotarlismy do s
        return
    for edge in v.prev:
        if Visited[edge.id]==0:
            Visited[edge.id]=1
            if Dist[edge.val][edge.id]==0:
                Dist[edge.val][n]+=1
                Dist[edge.val][n+1]=edge.id
            Dist[edge.val][edge.id]+=1
            DFS(edge, Visited, n, Dist)
    return

def enlarge(T, s, t): #główna funkcja algorytmu
    V=[Vertex(-1, [], [], i) for i in range(len(T))] #val=-1 <==> visited=False
    for i in range(len(T)): #zczytuję dane do klasy Vertex
        for edge in T[i]:
            V[i].edges.append(V[edge])
    q=Queue() #tworzę kolejkę do BFS
    q.put(V[s])
    V[s].val=0
    while q.q_size()!=0:
        v=q.get()
        if V[t].val!=-1 and v.val>V[t].val: #w takim wypadku nie ma sensu kontynuować (optymalizacja gdy np t jesli względnie blisko s)
            break
        for edge in v.edges: #dla każdej krawędzi v
            if edge.val==-1: #jeśli nie była odwiedzona to ustalamy jej odległość i dodajemy skąd przyszliśmy
                edge.val=v.val+1
                edge.prev.append(v)
                q.put(edge)
            elif edge.val==v.val+1: #już tu byliśmy ale optymalnie szybko więc też dodajemy skąd przyszliśmy
                edge.prev.append(v)
    if V[t].val==-1: #nie da się dojść z s do t
        return None
    Visited=[0 for _ in range(len(T))] #tablica do powrotu w DFS
    Dist=[[0 for j in range(len(T)+2)] for _ in range(len(V))] #tablica odległości (ta o kótrej pisałem w opisie algorytmu)
    n=len(Dist)
    Dist[V[t].val][n]=1
    Dist[V[t].val][n+1]=V[t].id
    Visited[V[t].id]=1
    DFS(V[t], Visited, n, Dist)
    for row in range(len(Dist)):
        if Dist[row][n]==1:
            if row+1<len(Dist) and Dist[row+1][n]==1: #warunek z opisu algorytmu
                return (Dist[row][n+1], Dist[row+1][n+1])
    return None #skoro jeszcze się funkcja nie skończyła to znaczy że szukana krawędź nie istnieje

runtests(enlarge)
            