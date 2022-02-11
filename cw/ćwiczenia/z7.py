'''
class Employee:
    def __init__(self, fun, emp=[]):
        self.emp=emp
        self.f=-1
        self.g=0
        self.fun=fun

def rek(v):
    if len(v.emp)==0:
        v.f=v.fun
        return
    for empl in v.emp:
        if empl.f==-1:
            rek(empl)
        v.g+=empl.f
        v.f+=empl.g
    v.f+=v.fun+1

def main(dziekan):
    rek(dziekan)
    return max(dziekan.f, dziekan.g)

d1=Employee(3)
d2=Employee(2)
d3=Employee(1)
c1=Employee(12, [d1,d2,d3])
c2=Employee(3)
c3=Employee(5)
c4=Employee(9)
c5=Employee(11)
b1=Employee(7, [c1,c2])
b2=Employee(13, [c3])
b3=Employee(21, [c4,c5])
a1=Employee(12, [b1,b2,b3])
dziekan=a1
print(main(dziekan))
'''
'''
import math

'''
idea funkcji do wypisywania miast jest przedstawiona w linku dla tablicy: C=[["Wrocław", 0, 2], ["Paprykarz Szczeciński", 1, 3], ["Warszawa", 4, 3], ["Gdańsk", 2, 4], ["Kraków", 3, 1]]
link przedstawia zmianę ścieżki przy wypisywaniu
https://imgur.com/a/EraaE9W
'''

def partition(T, l, p): #normalny partition do quicksorta
    pivot=T[p][1]
    j=l
    for i in range(l, p):
        if(T[i][1]<=pivot):
            T[i], T[j] = T[j], T[i]
            j+=1
    T[p], T[j] = T[j], T[p]
    return j

def sortowańsko(T): #normalny quicksort
    l=0
    p=len(T)-1
    stack=[0]*len(T)
    stack[0]=[l, p]
    top=0
    while top>=0:
        l, p = stack[top]
        top-=1
        q=partition(T, l, p)
        if q-1>l:
            top+=1
            stack[top]=[l, q-1]
        if q+1<p:
            top+=1
            stack[top]=[q+1, p]
    return T

def diff(a, b): #jesli różnica pierwszych współrzędnych jest równa 0 to nie zmieniam kierunku
    if b[0]-a[0]!=0:
        return -1
    return 1

def rek(last, H, left, T): #rekurencyjna funkcja do wypisywania miast; można bardzo łatwo zrobić tą funkcję iteracyjnie (taka sama idea, całkowicie analogicznie), ale już zbyt zmęczony jestem patrzeniem w ten kod
    a=H[last[0]][last[1]] #zczytuję dane z tablicy H
    b=last #jw.
    if a!=(0,0): #rekurencyjnie schodzę do początku tablicy H po obranej ścieżce
        rek(a, H, left, T)
    global dir #zczytuję kierunek
    dir*=diff(a, b) #potencjalna zmiana kierunku
    if dir==1: #wypisywana ścieżka
        print(T[b[1]][0], end=", ")
    else:
        left.append(T[b[1]][0]) #druga ścieżka
    
def d(a, b): #funkcja licząca odległość 2 punktów
    x1, y1, x2, y2 = a[1], a[2], b[1], b[2]
    distance=math.sqrt( (x2-x1)**(2) + (y2-y1)**(2) )
    return distance

def tspf(i, j, F, D, H): #przepisana funkcja z wykładu
    if F[i][j]!=math.inf:
        return F[i][j]
    if i==j-1:
        minimum=math.inf
        for k in range(j-1):
            q=tspf(k, j-1, F, D, H)+D[k][j]
            if minimum > q:
                minimum=q
                H[i][j]=(k, i)
        F[j-1][j]=minimum
    else:
        q=tspf(i, j-1, F, D, H)+D[j-1][j]
        if F[i][j]>q:
            H[i][j]=(i, j-1)
            F[i][j]=q
    return F[i][j]

def bitonicTSP(T): #launcher
    if len(T)==1: #nie wymaga komentarza
        print(T[0][0])
        return 0
    elif len(T)==0:
        print("")
        return 0
    T=sortowańsko(T)
    D=[[d(T[i], T[j]) if j>i else 0 for j in range(len(T))] for i in range(len(T))] #nie trzeba wypelniac całej tablicy, wystarczy pół; pamięć nie ma takiego znaczenia
    F=[[math.inf for j in range(len(T))] for i in range(len(T)-1)] #jw; używane jest pół, ale pamięć nie ma takiego znaczenia
    H=[[(0,0) for j in range(len(T))] for i in range(len(T)-1)] #jw; tablica przechowuje poprzednie wywołanie funkcji (np jesli f(4,5) powstaje z f(3,4) to H zapisuje w miejscu [4][5] (3,4))
    F[0][1]=D[0][1]
    F[0][len(T)-1]=tspf(0, len(T)-1, F, D, H)+D[0][len(T)-1]
    H[0][len(T)-1]=(0, len(T)-2)
    last=(0, len(T)-1) #współrzędne ostatniego wywołania
    minimum=F[0][len(T)-1]
    for i in range(1,len(T)-1):
        F[i][len(T)-1]=tspf(i, len(T)-1, F, D, H)+D[i][len(T)-1]
        if minimum > F[i][len(T)-1]:
            minimum=F[i][len(T)-1]
            last=(i, len(T)-1)
    left=[]
    print(T[0][0], end=", ")
    rek(last, H, left, T)
    for el in left[::-1]:
        print(el, end=", ")
    print(T[0][0])
    print(minimum)
    return

dir=1 #nie usuwać!
C = [["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdańsk", 2, 4], ["Kraków", 3, 1]]
bitonicTSP(C)
'''
'''
from queue import PriorityQueue

S = ["a", "b", "c" ,"d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "u" ]
F = [1,1,1,1,1,1,2,2,2,2,2,2,3,4,4,7]

class Tree: #struktura przechowywująca wygląd drzewa budowanego przez algorytm kodu Huffmana
    def __init__(self, val, id, left=None, right=None): #val-częstość, id-pozycja w tablicy liter, left-lewe dziecko, right-prawe dziecko
        self.val=val
        self.id=id
        self.left=left
        self.right=right
    #klasa PriorityQueue nie może porównywać elementów Tree, bo sama nie umie się domyśleć, że należy porównywać element1.val i element2.val
    #poniższe linijki służą umożliwieniu PriorityQueue porównywania elementów Tree (przekopiowane i zparafrazowane z jakiegoś stacka, ale nie stanowi to części merytorycznej zadania, więc uznałem, że można)
    def __gt__(self, other):
        return self.val>other.val
    def __ge__(self, other):
        return self.val>=other.val
    def __eq__(self, other):
        return self.val==other.val
    def __lt__(self, other):
        return self.val<other.val
    def __le__(self, other):
        return self.val<=other.val

def wypisz(root, T, N, wynik=""): #funkcja co prawda nie wypisuje wyniku jak wskazuje nazwa, ale przygotowuje dane aby można było je wypisać dokładnie w formie podanej w treści
    if root.left is not None: #istnieje lewe dziecko
        wypisz(root.left, T, N, wynik+"0") #idziemy w lewo, więc dopisujemy 0 do wyniku
    if root.right is not None: #istnieje prawe dziecko
        wypisz(root.right, T, N, wynik+"1") #idziemy w prawo, więc dopisujemy 1 do wyniku
    if root.id is not None: #doszliśmy na sam dół drzewa
        global suma #wczytujemy sumę (długość napisu)
        suma+=root.val*len(wynik) #suma zwiększa się o częstość*binarna długość znaku 
        N[root.id]="{} : {}".format(T[root.id], wynik) #ustawiamy daną literę z jej binarnym zapisem w odpowiednim miejscu do wypisania
    return

def huffman(T, F):
    q=PriorityQueue() #inicjalizacja PriorityQueue pod zmienną q
    for i in range(len(T)): #wypełnianie q
        q.put(Tree(F[i], i)) #utwarzanie odpowiednich obiektów jako elementów q
    while q.qsize()>1: #pętla ma się kończyć, gdy w q zostanie 1 element (root)
        l=q.get() #ściągam 2 elementy z q: najmniejszy i 2gi najmniejszy
        p=q.get()
        if p.val>=l.val: #ten prosty przypadek, że drugi element jest większy bądź równy najmniejszemu
            new=Tree(l.val+p.val, None, left=l, right=p) #łączę je w nowy obiekt o częstości równej ich sumie
            q.put(new) #dodaję do q
        else: #ten drugi przypadek
            if q.empty() is False: #chcę ściągnąć kolejny element
                r=q.get() #ściągam pozostały najmniejszy element
                new=Tree(r.val+p.val, left=p, right=r) #łącze licząc na to, że w następnym przebiegu pętli p będzie większe od l
                q.put(l)
                q.put(new)
            else: #ostatni krok
                new=Tree(l.val+p.val, None, left=l, right=p)
                q.put(new)
    root=q.get() #ściągam pozostały element
    wypisz(root, T, F) #żeby nie marnować pamięci nie tworzę nowej tablicy do wywołania danych tylko zamieniam nieużywaną F
    for el in F:
        print(el)
    global suma
    print("dlugosc napisu: ", suma)
    return
  
suma=0 #za pomocą tej globalnej zmiennej długość napisu będzie wyliczana
huffman( S, F )
'''