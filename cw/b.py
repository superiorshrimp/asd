'''
#odwracanie Node'a
class Node:
    def __init__(self, val, next=None):
        self.val=val
        self.next=next

def add(head, value):
    new=Node(value)
    if head is None:
        return new
    elif head.next is None:
        head.next=new
        return head
    curr=head
    prev=None
    while curr is not None:
        prev=curr
        curr=curr.next
    prev.next=new
    return head

def show(head):
    while head is not None:
        print(head.val, end=' ')
        head=head.next
    return
#1 2 3 4 5 6
def reverse(head, prev):
    if head is None:
        return prev
    copy=head
    copy_prev=prev
    prev=head
    head=head.next
    copy.next=copy_prev
    return reverse(head, prev)

head=None
for i in range(10):
    head=add(head, i**2)
head=reverse(head, None)
show(head)
'''
'''
Zadanie 6. (wyszukiwanie binarne) Proszę zaimplementować funkcję,
która otrzymuje na wejściu posortowaną niemalejąco tablicę A o rozmiarze n oraz liczbę x i sprawdza, czy x występuje w A.
Jeśli tak, to zwraca najmniejszy indeks, pod którym x występuje.
'''
'''
def binary_search(T, x):
    l=0
    p=len(T)-1
    while(l+1!=p):
        avg=(l+p)//2
        if(x>T[avg]):
            l=avg
        elif(x<T[avg]):
            p=avg
        else:
            print("there it is!")
            while(avg>=0):
                avg-=1
                if(T[avg]!=x):
                    return avg+1
            return 
    print("nei")
    return None

T=[13, 24, 35, 46, 56, 67, 78, 89, 543]
print(binary_search(T, 46))
'''
'''
#Input:  { 2, 0, 2, 1, 4, 3, 1, 0 }
#Output: The largest subarray is { 0, 2, 1, 4, 3 }
def f(T):
    W=[]
    max=0
    for i in range(len(T)):
        print(W, i)
        if T[i] not in W: #TODO: quick search; sortowanie
            W.append(T[i])
            if(len(W)>max):
                max=len(W)
        else:
            while T[i] in W[0:-2]:
                del W[0]
    return max

T=[ 2, 0, 2, 2, 1, 4, 3, 1, 0 ]
print(f(T))
#kinda
'''
'''
#Input: { 0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0 }
#Output:{ 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2 }

def f(T):
    l=0
    p=len(T)-1
    for i in range(len(T)):
        while True:
            if(T[i]==0 and l<i):
                T[l], T[i] = 0, T[l]
                l+=1
            elif(T[i]==2 and p>i):
                T[p], T[i] = 2, T[p]
                p-=1
            else:
                break
            print(T, i, l, p)
    return T

T=[0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]
print(f(T))
'''
'''
#The longest bitonic subarray of the sequence { 3, 5, 8, 4, 5, 9, 10, 8, 5, 3, 4 } is { 4, 5, 9, 10, 8, 5, 3 }

def f(T):
    if(len(T)==0):
        return 0
    maxi=0
    asc=0
    des=0
    last=0
    per=None
    for i in range(len(T)-1):
        if(T[i+1]>T[i]):
            if(per==False): #False - rosnace
                last=des
                des=0
            per=True
            asc+=1
            if(asc+max(des, last)>maxi):
                maxi=asc+des
        elif(T[i+1]>T[i]):
            if(per==True): #true - rosnace
                last=asc
                asc=0
            per=False
            des+=1
            if(des+max(asc, last)>maxi):
                maxi=asc+des
        else:
            last=0
    return maxi+1

T=[3, 5, 8, 4, 5, 9, 10, 8, 5, 3, 4]
print(f(T))
'''
'''
3. Proszę opisać (bez implementacji!) jak najszybszy algorytm, który otrzymuje na wejściu pewien
ciąg n liter oraz liczbę k i wypisuje najczęściej powtarzający się podciąg długości k (jeśli ciągów
mogących stanowić rozwiązanie jest kilka, algorytm zwraca dowolny z nich). Można założyć, że
ciąg składa się wyłącznie z liter a i b.
Na przykład dla ciągu ababaaaabb oraz k = 3 rozwiązaniem jest zarówno ciąg aba, który
powtarza się dwa razy (to, że te wystąpienia na siebie nachodzą nie jest istotne). Zaproponowany
algorytm opisać, uzasadnić jego poprawność oraz oszacować jego złożoność.

def binarnie(wyraz):
    suma=0
    for i in range(len(wyraz)):
        if(wyraz[i]=="a"):
            suma+=2**(i)
    return suma

def f(ciag, k):
    W=[0 for _ in range(k**2)]
    for i in range(len(ciag)-k+1):
        W[binarnie(ciag[i:i+3])]+=1
    max=0
    for el in W:
        if el>max:
            max=el
    return max


ciag="ababaaaabb"
k=3
print(f(ciag, k))
'''
'''
1. Dana jest struktura opisująca listę jednokierunkową dla liczb rzeczywistych:
struct Node{ Node* next; double value; }
Proszę zaimplementować funkcję void Sort( Node* list ), która otrzymuje na wejściu listę
liczb rzeczywistych (z wartownikiem), wygenerowaną zgodnie z rozkładem jednostajnym na
przedziale [0,10) i sortuje jej zawartość w kolejności niemalejącej. Funkcja powinna być możliwie
jak najszybsza (biorąc pod uwagę warunki zadania). Proszę oszacować złożoność
zaimplementowanej funkcji.

import random

class Node:
    def __init__(self, val, next=None):
        self.val=val
        self.next=next

def utworz_linkliste_z_listy(T):
    if(len(T)==0):
        return None
    zbior=Node(T[0])
    kopia=zbior
    for k in T[1:]:
        nowy=Node(k)
        kopia.next=nowy
        kopia=kopia.next
    return zbior

def wypisz(zbior):
    if zbior is None:
        print("pusty")
        return
    while zbior is not None:
        print(zbior.val, end=" ")
        zbior=zbior.next
    print()
    return
'''
'''
def merge(head): #insertion sort
    curr=head.next
    prev=head
    while curr is not None:
        if(curr.val<=head.val):
            prev.next=curr.next
            curr.next=head
            head=curr
            curr=prev
        else:
            cp=head.next
            previous=head
            while curr.val>cp.val and cp!=curr:
                previous=cp
                cp=cp.next
            if(cp!=curr):
                prev.next=curr.next
                curr.next=previous.next
                previous.next=curr
                curr=prev
        prev=curr
        curr=curr.next
    return head
'''
'''
def bucket_sort(head, i, dokl):
    if(i==dokl):
        curr=head
        prev=None
        while curr is not None:
            prev=curr
            curr=curr.next
        if prev is None:
            prev=head
        return head, prev #sa sobie rowne (wartosciami)
    W=[[None, None] for _ in range(10)] #W=[head, last]
    while head is not None:
        if W[int(head.val*10**i)%10][0] is not None:
            W[int(head.val*10**i)%10][1].next=head
            tmp=head
            W[int(head.val*10**i)%10][1]=head
            head=head.next
            tmp.next=None
        else:
            W[int(head.val*10**i)%10][0]=head
            W[int(head.val*10**i)%10][1]=head
            tmp=head
            head=head.next
            tmp.next=None
    first_not_None=None
    last_not_None=None
    for el in W:
        if el[0] is not None:
            if first_not_None is None:
                first_not_None=el[0]
            if(el[0]!=el[1]):
                el[0], el[1]=bucket_sort(el[0], i+1, dokl)
            if last_not_None is not None:
                last_not_None.next=el[0]
            last_not_None=el[1]
    return first_not_None, last_not_None
        
def Sort(head):
    dokl=8 #x.xxxx xxxx
    if head is None:
        return
    else:
        bucket_sort(head, 0, dokl)
        return

head=None
T=[round(random.uniform(0,10),8-1) for _ in range(10)]
print(T)
head=utworz_linkliste_z_listy(T)
Sort(head)
wypisz(head)
#do skonczenia
'''
'''
Consider S = {3, 1, 1, 2, 2, 1}
We can partition S into two partitions, each having a sum of 5.
S1 = {1, 1, 1, 2}
S2 = {2, 3}
Note that this solution is not unique. Here’s another solution.
S1 = {3, 1, 1}
S2 = {2, 2, 1}
''' 
'''
Input:
A = [2, 1, 3, 5, 4, 7, 6, 8, 9]
x = 5
Output: Element 5 found at index 3
Input:
A = [2, 1, 3, 5, 4, 7, 6, 8, 9]
x = 10
Output: Element not found in the array

def f(T, l, p, x):
    mid=(l+p)//2
    if(x==T[mid] or (mid-1>0 and T[mid-1]==x) or (mid+1<len(T) and T[mid+1]==x)):
        return True
    elif(): #i dalej jak binary search
'''
'''
Input:  {2, 1, -5, 4, -3, 1, -3, 4, -1}
Output: Subarray with the largest sum is {4, -1, 2, 1} with sum 6.
Input:  {-3, 1, -3, 4, -1, 2, 1, -5, 4}
Output: Subarray with the largest sum is {4, -1, 2, 1} with sum 6.
'''
'''
def f(T): #SSP
    max=0
    sumb=0
    start=0
    end=0
    suma=0
    max_sumb=0
    for i in range(len(T)):
        sumb+=T[i]
        if(sumb>max_sumb):
            max_sumb=sumb
            end=i
        suma+=T[i]
        if(suma<0):
            suma=0
            start=i+1
        else:
            if(suma>max):
                max=suma
                if(i==len(T)-1):
                    print("a")
                    if(max_sumb>0 and start>end):
                        max=max+max_sumb
    i=len(T)-1
    begin=len(T)-1
    sumbe=0
    max_sumbe=0
    while i>=0:
        sumbe+=T[i]
        if(sumbe>max_sumbe):
            max_sumbe=sumbe
            begin=i
        i-=1

    if(max_sumbe+max_sumb>max and begin>end):
        return max_sumbe+max_sumb

    return max

T=[1000, -10000, 1001, -10000, 1000]
print(f(T))
#zle: reverse Kadane's algorytm
'''
'''
#21:52
uzycie sortowania do rozwiazania zadania powodowalo by zlozonosc nlogn (sortowanie nlogn + sumowanie n)
innym podejsciem byloby uzycie heapsort co jednak ostatecznie stanowiloby zlozonosc nlogn (heapsort do odpowiednio fromtego lub totego elementu)
postanowilem uzyc magiczne piatki aby najpierw ograniczyc zakres poszukiwan a potem wyznaczyc znalezc from i to (logn)
nastepnie zsumowalem elementy pomiedzy (n) wiec zlozonosc O to n co jest lepsze niz 2 powyzsze metody dajace zlozonosc nlogn 
import random

def partition(T, l, p):
    pivot=T[p]
    j=l
    for i in range(l,p):
        if T[i]<=pivot:
            T[j], T[i] = T[i], T[j]
            j+=1
    return j

def magiczne_piatki(T, l, p, k):
    q=partition(T, l, p)
    if k<q:
        return magiczne_piatki(T, l, q-1, k)
    elif k>q:
        return magiczne_piatki(T, q+1, p, k)
    else:
        return q

def sum_between(T, l, p, fr, to):
    q=partition(T, l, p)
    if(q<fr):
        return sum_between(T, q+1, p, fr, to)
    elif(q>to):
        return sum_between(T, l, q-1, fr, to)
    else:
        l, s1 = magiczne_piatki(T, l, q, fr)
        p, s2 = magiczne_piatki(T, q, p, to)
        suma=s1+s2
    return suma


T=[random.randint(0,1000) for _ in range(100)]
fr=10
to=len(T)-20
print(sum_between(T, 0, len(T)-1, fr, to))
sorted(T)
suma=0
for i in range(fr, to+1):
    suma+=T[i]
print(suma)
'''
'''
#srednia ptej do ktej liczby w tablicy

def heapify_max(T, i, size):
    l=2*i+1
    p=2*i+2
    if(l<size):
        if(p<size):
            if(T[l]>=T[p]):
                if(T[i]<T[l]):
                    T[i], T[l] = T[l], T[i]
                    heapify_max(T, l, size)
            else:
                if(T[i]<T[p]):
                    T[i], T[p] = T[p], T[i]
                    heapify_max(T, p, size)
        else:
            if(T[i]<T[l]):
                T[i], T[l] = T[l], T[i]
                heapify_max(T, l, size)


def heapify_min(T, i, size):
    l=2*i+1
    p=2*i+2
    if(l<size):
        if(p<size):
            if(T[l]<=T[p]):
                if(T[i]>T[l]):
                    T[i], T[l] = T[l], T[i]
                    heapify_min(T, l, size)
            else:
                if(T[i]>T[p]):
                    T[i], T[p] = T[p], T[i]
                    heapify_min(T, p, size)
        else:
            if(T[i]>T[l]):
                T[i], T[l] = T[l], T[i]
                heapify_min(T, l, size)

def heap_insert_max(T, el):
    T.append(el)
    i=len(T)-1
    while (i-1)//2>=0:
        if(T[(i-1)//2]<T[i]):
            T[(i-1)//2], T[i] = T[i], T[(i-1)//2]
            i=(i-1)//2
        else:
            return

def heap_insert_min(T, el):
    T.append(el)
    i=len(T)-1
    while (i-1)//2>=0:
        if(T[(i-1)//2]>T[i]):
            T[(i-1)//2], T[i] = T[i], T[(i-1)//2]
            i=(i-1)//2
        else:
            return

def f(T, lowest, highest): #zał: highest>lowest
    suma=T[0]
    min_heap=[T[0]] #zbiera highest najwiekszych wartosci
    max_heap=[T[0]] #zbiera lowest najnizszych wartosci
    j=1

    while len(min_heap)<highest and len(max_heap)<lowest:
        heap_insert_max(max_heap, T[j])
        heap_insert_min(min_heap, T[j])
        suma+=T[j]
        j+=1
    s1=s2=suma #s1 od heap max; s2 od heap min

    while len(min_heap)<highest:
        if T[j]<=max_heap[0]:
            s2=s2-max_heap[0]+T[j]
            max_heap[0]=T[j]
            heapify_max(max_heap, 0, len(max_heap))
        suma+=T[j]
        s1+=T[j]
        j+=1

    while len(max_heap)<lowest:
        if T[j]>=min_heap[0]:
            s1=s1-min_heap[0]+T[j]
            min_heap[0]=T[j]
            heapify_min(min_heap, 0, len(min_heap))
        suma+=T[j]
        s2+=T[j]
        j+=1

    for i in range(j, len(T)):
        suma+=T[i]
        if T[i]<=max_heap[0]:
            s2=s2-max_heap[0]+T[i]
            max_heap[0]=T[i]
            heapify_max(max_heap, 0, len(max_heap))
        elif T[i]>=min_heap[0]:
            s1=s1-min_heap[0]+T[i]
            min_heap[0]=T[i]
            heapify_min(min_heap, 0, len(min_heap))
    
    return (suma-s1-s2)/(len(T)-len(max_heap)-len(min_heap))

T=[1, 4, 3, 5, 2, 7, 9, 12, 15, 10]
print(f(T, 2, 2))
print(sorted(T))
'''
'''
def partition(T, l, p):
    a=randint(l, p)
    pivot=T[a][0]
    T[a], T[p] = T[p], T[a]
    j=l
    for i in range(l, p):
        if(T[i][0]<=pivot):
            T[i], T[j] = T[j], T[i]
            j+=1
    T[p], T[j] = T[j], T[p]
    return j

def quicksort(T): #iteracyjnie
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

def sum_sort(A, B, n):
    W=[]
    suma=0
    for i in range(len(A)):
        suma+=A[i]
        if (i+1)%n==0:
            W.append((suma, i//n))
            suma=0
        i+=1
    quicksort(W)
    for el in W:
        for i in range(n):
            B[n*el[1]+i]=A[n*el[1]+i]
    return B
'''
'''
#Dana jest tablica liczb rzeczywistych wielkości n reprezentująca kopiec minimum (array-based heap).
#Mając daną liczbę rzeczywistą x sprawdź, czy k-ty najmniejszy element jest większy lub równy x.

from random import randint

def heapify(T, i, size):
    l=2*i+1
    p=2*i+2
    if(l<size):
        if(p<size):
            if(T[l]<=T[p]):
                if(T[i]>T[l]):
                    T[i], T[l] = T[l], T[i]
                    heapify(T, l, size)
            else:
                if(T[i]>T[p]):
                    T[i], T[p] = T[p], T[i]
                    heapify(T, p, size)
        else:
            if(T[i]>T[l]):
                T[i], T[l] = T[l], T[i]
                heapify(T, l, size)

def build_heap(T):
    for i in range(len(T)//2, -1, -1):
        heapify(T, i, len(T))

def f(T, i, x): # dodac global licznik zeby nie sprawdzac niepotrzebnie
    if i>=len(T):
        return 0
    if T[i]<x:
        return 1+f(T, 2*i+1, x)+f(T, 2*i+2, x)
    else:
        return 0

def main(T, k, x):
    q=f(T, 0, x)
    if q<k+1:
        return True
    return False

T=[randint(0,100) for _ in range(10)]
build_heap(T)
k=5
print(main(T, k, 50))
T=sorted(T)
print(T[k], T)
'''
'''
#Dana jest posortowana rosnąco tablica A wielkości n zawierająca parami różne liczby naturalne. Podaj algorytm, który sprawdzi, czy jest taki indeks i, że
#A[i] == i.
#Co zmieni się, jeżeli liczby będą po prostu całkowite, niekoniecznie naturalne?
#naturalne - wystarczy T[0] sprawdzic
def f_c(T, l, p):
    if p<l:
        return False
    mid=(l+p)//2
    if T[mid]<mid:
        return f_c(T, mid+1, p)
    elif T[mid]>mid:
        return f_c(T, l, mid-1)
    else:
        return mid

def f_calkowite(T):
    return f_c(T, 0, len(T)-1)

T=[-7,-3,-1,0,3,4,12]
print(f_calkowite(T))
'''
'''
#Dana jest tablica A oraz liczba k. Znaleźć liczbę różnych par elementów z tablicy A o różnicy równej k.
#Przykład: Dla tablicy [7,11,3,7,3,9,5] oraz k = 4 odpowiedź to 3


def f(T, k):
    T=sorted(T)
    start=0
    licznik=0
    W=[]
    last=T[0]
    for i in range(1,len(T)): # n
        if T[i]!=last:
            W.append(T[i])
        last=T[i]
    for i in range(len(T)):
        while T[i]>T[start]+k:
            start+=1
        if T[i]==T[start]+k:
            licznik+=1
    return licznik

k=4
T=[7,11,3,7,3,9,5]
print(f(T, k))
'''
'''
Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie jeden raz.
Cyfra wielokrotna to taka, która w liczbie występuje więcej niż jeden raz. 
Mówimy, że liczba naturalna A jest ładniejsza od liczby naturalnej B, jeżeli w liczbie A występuje więcej cyfr jednokrotnych niż w B,
a jeżeli cyfr jednokrotnych jest tyle samo to ładniejsza jest ta liczba, która posiada mniej cyfr wielokrotnych.
Na przykład: liczba 123 jest ładniejsza od 455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne.
Dana jest tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję: pretty_sort(T),
która sortuje elementy tablicy T od najładniejszych do najmniej ładnych.

def f(n):
    Count=[0 for _ in range(10)]
    single=0
    multi=0
    while n!=0:
        q=n%10
        if Count[q]==0:
            single+=1
        elif Count[q]==1:
            multi+=1
            single-=1
        Count[q]+=1
        n//=10
    return single, multi

def radix_sort(T, k): # po k-tym indeksie
    Count=[0 for _ in range(10)]
    for i in range(len(T)):
        Count[9-T[i][k]]+=1
    W=[0]*len(T)
    for i in range(1,10):
        Count[i]+=Count[i-1]
    for i in range(len(T)):
        Count[9-T[i][k]]-=1
        W[Count[9-T[i][k]]]=T[i]
    return W

def pretty_sort(T):
    for i in range(len(T)):
        a, b = f(T[i])
        T[i]=(T[i], a, b)
    T=radix_sort(T, 2)
    T=radix_sort(T, 1)
    for i in range(len(T)):
        T[i]=T[i][0]
    return T

T=[123,455,1266,114577,2344,67333]
print(pretty_sort(T))
'''
'''
from random import randint

def center(T):
    suma=0
    for el in T:
        suma+=el
    avg=suma/len(T)
    min_id=0
    min=abs(T[0]-avg)
    for i in range(len(T)):
        if abs(T[i]-avg)<min:
            min=abs(T[i]-avg)
            min_id=i
    suma=0
    for el in T:
        suma+=abs(el-T[min_id])
    return T[min_id], suma

def median(T):
    T=sorted(T)
    if len(T)%2==1:
        suma=0
        for el in T:
            suma+=abs(el-T[len(T)//2])
        return T[len(T)//2], suma

    else:
        suma=0
        for el in T:
            suma+=abs(el-T[len(T)//2])
        #suma1=0
        #for el in T:
            #suma1+=abs(el-T[len(T)//2+1])
        return T[len(T)//2], suma #T[len(T)//2+1], suma, suma1

def check(T):
    min=9999
    for i in range(len(T)):
        suma=0
        for el in T:
            suma+=abs(el-T[i])
        if suma<min:
            min=suma
            min_id=i
    return T[min_id], min

T=[]
while len(T)<10:
    a=randint(-10, 10)
    while a in T:
        a=randint(-10, 10)
    T.append(a)

print(center(T), median(T), check(T))    
print(sorted(T))
'''
'''
def merge_two_sorted_nodes(head1, head2): #bez tworzenia nowego node'a
    if head1 is None:
        return head2
    elif head2 is None:
        return head1
    if head1.val>head2.val:
        head2, head1 = head1, head2
    curr1=head1.next
    prev1=head1
    while curr1 is not None and head2 is not None:
        if curr1.val>head2.val:
            new=head2
            head2=head2.next
            prev1.next=new
            new.next=curr1
            prev1=new
        else:
            prev1=curr1
            curr1=curr1.next
    if curr1 is None:
        prev1.next=head2
    return head1

def merge_natural_series_node(head):
    T=[]
    curr=head.next
    prev=head
    new_head=prev
    while curr is not None:
        if curr.val<prev.val:
            T.append(new_head)
            prev.next=None
            new_head=curr
        prev=curr
        curr=curr.next
    T.append(new_head)
    while len(T)!=1:
        W=[]
        for i in range(0, len(T)-1, 2):
            W.append(merge_two_sorted_nodes(T[i], T[i+1]))
        if len(T)%2==1:
            W.append(T[len(T)-1])
        T=W
    return T[0]


T=[randint(0,100) for _ in range(2)]
head=utworz_linkliste_z_listy(T)
wypisz(head)
head=merge_natural_series_node(head)
wypisz(head)
print(sorted(T))
'''
'''
#przedzial najwiecej przedzialow n^2
def partition_x(T, l, p):
    pivot=T[p][0]
    j=l
    for i in range(l, p):
        if(T[i][0]<=pivot):
            T[i], T[j] = T[j], T[i]
            j+=1
    T[p], T[j] = T[j], T[p]
    return j

def quicksort_x(T): #iteracyjnie
    l=0
    p=len(T)-1
    stack=[0]*len(T)
    stack[0]=[l, p]
    top=0
    while top>=0:
        l, p = stack[top]
        top-=1
        q=partition_x(T, l, p)
        if q-1>l:
            top+=1
            stack[top]=[l, q-1]
        if q+1<p:
            top+=1
            stack[top]=[q+1, p]
    return T

def partition_y(T, l, p):
    pivot=T[p][1]
    j=l
    for i in range(l, p):
        if(T[i][1]>=pivot):
            T[i], T[j] = T[j], T[i]
            j+=1
    T[p], T[j] = T[j], T[p]
    return j

def quicksort_y(T): #iteracyjnie; nierosnace
    l=0
    p=len(T)-1
    stack=[0]*len(T)
    stack[0]=[l, p]
    top=0
    while top>=0:
        l, p = stack[top]
        top-=1
        q=partition_y(T, l, p)
        if q-1>l:
            top+=1
            stack[top]=[l, q-1]
        if q+1<p:
            top+=1
            stack[top]=[q+1, p]
    return T

def f(T): #n^2
    max=0
    max_id=0
    quicksort_y(T) #sortowanie po y malejaco; nlogn
    quicksort_x(T) #sortowanie po x; nlogn
    for i in range(len(T)): #n
        licznik=0
        j=i+1
        while j<len(T): #n
            if T[j][1]<=T[i][1]:
                licznik+=1
                if licznik>max:
                    max_id=i
                    max=licznik
                j+=1
            else:
                break
    return T, max_id, max

T=[(1, 3), (2, 4), (7, 15), (0, 10), (1, 2), (1, 5)]
print(f(T))
'''
'''
from random import randint

def partition(T, l, p):
    pivot=T[p]
    j=l
    for i in range(l, p):
        if T[i]>=pivot:
            T[i], T[j] = T[j], T[i]
            j+=1
    T[p], T[j] = T[j], T[p]
    return j

def find_kth(T, l, p, k):
    q=partition(T, l, p)
    if q<k:
        find_kth(T, q+1, p, k)
    elif q>k:
        find_kth(T, l, q-1, k)
    else:
        return

def f(T, p, q, start, stop):
    k=partition(T, start, stop)
    if k<p:
        return f(T, p, q, k+1, stop)
    elif k>q:
        return f(T, p, q, start, k-1)
    else:
        if k!=p:
            find_kth(T, start, k-1, p)
        if k!=q:
            find_kth(T, k+1, stop, q)
    return T[p:q+1]

def section(T, p, q):
    return f(T, p, q, 0, len(T)-1)

T=[randint(0,100) for _ in range(10)]
print(T)
print(section(T, 0, 3))
print(T)
print("a")
T=sorted(T)
print(T)
print(T[6:10])
'''
'''
def insertion_sort_node(head):
    if head is None or head.next is None:
        return head
    curr=head.next
    prev=head
    i=1
    while curr is not None:
        if(promien(curr.val)<promien(head.val)):
            prev.next=curr.next
            curr.next=head
            head=curr
            curr=prev
        else:
            j=1
            copy=head.next
            copy_prev=head
            while(promien(curr.val)>promien(copy.val) and j<i):
                j+=1
                copy_prev=copy
                copy=copy.next
            if(j!=i):
                prev.next=curr.next
                curr.next=copy
                copy_prev.next=curr
                curr=prev
        i+=1
        prev=curr
        curr=curr.next
    return head

def promien(krotka):
    r=(krotka[0]**2+krotka[1]**2)**(0.5)
    return r
    
def przedzialy(const, var_r, points_r, i):
    if i==0:
        return 0
    new_r=(var_r**2-const)**(0.5)
    if new_r<=points_r:
        return i
    else:
        return przedzialy(const, new_r, points_r, i-1)

def f(T, R): # r - promień
    const=(R**2)/len(T)
    Buckets=[None]*len(T) # dodac node
    for el in T:
        id=przedzialy(const, R, promien(el), len(T)-1)
        if Buckets[id] is None:
            new=Node(el)
        else:
            new=Node(el, Buckets[id])
        Buckets[id]=new    
    W=[]
    for el in Buckets:
        el=insertion_sort_node(el)
        while el is not None:
            W.append(el.val)
            el=el.next
    return W

T=[]
for _ in range(10):
    a,b = round(uniform(-1,1),4), round(uniform(-1,1),4)
    while promien((a,b))>1:
        a,b = round(uniform(-1,1),4), round(uniform(-1,1),4)
    T.append((a,b))
T=f(T, 1)
for el in T:
    print(promien(el))
'''
'''from random import randint

def sort_012(T):
    l=0
    p=len(T)-1
    i=0
    while p>0 and T[p]==2:
        p-=1
    while l<=p and T[l]==0:
        i+=1
        l+=1
    while i<=p:
        print(T, i, l, p)
        if T[i]==0:
            T[i], T[l] = T[l], T[i]
            l+=1
        elif T[i]==2:
            T[i], T[p] = T[p], T[i]
            if T[i]==0:
                T[i], T[l] = T[l], T[i]
                l+=1
            while p>l and T[p]==2:
                p-=1

        i+=1
    return T

T=[randint(0,2) for _ in range(randint(1,10))]
print(T)
print(sort_012(T))
#dutch flag
'''
'''
def f(T, k):
    W=[[len(T)+1 for col in range(k+1)] for row in range(len(T))]
    mini=len(T)+1
    start=0
    while T[start]>k:
        start+=1
    if T[start]==k:
        return 1
    W[start][T[start]]=1
    for i in range(start+1,len(T)):
        W[i][T[i]]=1
        for j in range(k):
            if W[i-1][j]>0:
                if j+T[i]<k:
                    W[i][j+T[i]]=min(W[i][j+T[i]], W[i-1][j]+1)
                elif j+T[i]==k:
                    W[i][j+T[i]]=min(W[i][j+T[i]], W[i-1][j]+1)
                    mini=min(mini, W[i][j+T[i]])
                W[i][j]=min(W[i][j], W[i-1][j])
    return mini

T=[1,2,3,5,15,7]
print(f(T, 27))
'''
'''
def f(source, target):
    omax=0
    T=[[0 for i in range(len(source))] for letter in range(len(target))]
    for i in range(len(source)):
        if source[i]==target[0]:
            T[0][i]=1
    for i in range(1,len(target)):
        maks=T[i-1][0]
        omax=max(omax, maks)
        if source[0]==target[i]:
            T[i][0]=1
        else:
            T[i][0]=T[i-1][0]
        for j in range(1,len(source)):
            maks=max(maks-1, T[i-1][j-1])
            omax=max(omax, maks)
            if source[j]==target[i]:
                T[i][j]=maks+1
            else:
                T[i][j]=maks
    for el in T:
        print(el)
    return len(target)-omax
print(f("abcedef", "abgdeg"))
'''
'''
def f(T):
    W=[[0 for i in range(len(T))] for j in range(4)]
    for index in range(0, len(T)-3):
        W[0][index]=-T[index]
    for i in range(1,4):
        maks=W[i-1][i-1]
        for index in range(i, len(T)-3+i):
            maks=max(maks, W[i-1][index-1])
            if (i+1)%2==0:
                W[i][index]=maks+T[index]
            else:
                W[i][index]=maks-T[index]
    for el in W:
        print(el)
    for lm in el:
        maks=max(maks, lm)
    return maks

print(f( [3, 9, 10, 1, 30, 40] ))
'''
'''
#ciecie preta
def f(P):
    n=len(P)
    T=[P[i] for i in range(n)]
    for i in range(1,n+1):
        for j in range(i+1):
            T[i]=max(T[i], T[j]+P[i])
    return T[n-1]

P=[0,2,2,7,5,3]
print(f(P))
'''
'''
#schody amazona
def f(T):
    W=[0 for _ in range(len(T))]
    W[0]=1
    for i in range(len(T)-1):
        for j in range(1,T[i]+1):
            W[i+j]+=W[i]
    print(W)
    return W[len(T)-1]

T=[2,1,3,2,1,0]
print(f(T))
'''
'''
#najtansza droga od 0,0 do len t -1, len t[0] -1
def f(T):
    W=[[T[j][i] for i in range(len(T[0]))] for j in range(len(T))]
    for el in W:
            print(el)
    for i in range(len(T)):
        for j in range(len(T[0])):
            if i-1>=0:
                if j-1>=0:
                    W[i][j]+=min(W[i-1][j], W[i][j-1])
                else:
                    W[i][j]+=W[i-1][j]
            elif j-1>=0:
                W[i][j]+=W[i][j-1]
    return W[len(T)-1][len(T[0])-1]

T=[
    [3,4,5,2,1],
    [7,2,13,7,8],
    [3,1,4,6,5],
    [2,8,11,10,3],
    [3,5,1,6,2]
]
print(f(T))
'''
'''
#najdluzsza rosnaca sciezka; start w danym punkcie
def f(T, W, row, col, ruchy):
    global maks
    for ruch in ruchy:
        if 0<=row+ruch[0]<len(T) and 0<=col+ruch[1]<len(T) and T[row+ruch[0]][col+ruch[1]]>T[row][col] and W[row+ruch[0]][col+ruch[1]]==1:
            W[row+ruch[0]][col+ruch[1]]=1+W[row][col]
            maks=max(maks, W[row+ruch[0]][col+ruch[1]])
            f(T, W, row+ruch[0], col+ruch[1], ruchy)
    return

def launcher(T, row, col):
    global maks
    W=[[1 for i in range(len(T[0]))] for j in range(len(T))]
    ruchy=((1,0), (0,1), (0,-1), (-1,0))
    f(T, W, row, col, ruchy)
    for el in W:
        print(el)
    return maks

T=[
    [3,4,5,2,1],
    [7,2,13,7,8],
    [3,1,4,6,5],
    [2,8,11,10,3],
    [3,5,1,6,2]
]

maks=1
print(launcher(T, 0, 0))
'''
'''
def coins2( x, M ):
    T=[x+1 for _ in range(x+1)]
    T[0] = 0
    for y in range(x+1):
        for m in M:
            if y >= m:
               T[y] = min(T[y],T[y-m]+1)
    print(T)
    return T[x]
'''
'''
def f(t, S):
    W=[[0 for j in range(len(t))] for i in range(len(t))]
    for i in range(len(t)): #litera z t
        for s in S: #słowo z S
            if i+1>=len(s) and s==t[i-len(s)+1:i+1]:
                W[i-len(s)+1][i]=max(W[i-len(s)+1][i], len(s))
                W[0][i]=max(W[0][i], min(W[0][i-len(s)], len(s)))
    for el in W:
        print(el)
    return W[0][len(t)-1]
t="ababbab"
S=[
    "ab",
    "abab",
    "ba",
    "bab",
    "b"
t="paarapapapa"
S=["pa", "ara", "ap", "papa"]
print(f(t, S))
'''
'''
def f(N, t):
    H=[[N[i][j] for j in range(len(N[0]))] for i in range(len(N))]
    for i in range(len(N)):
        for j in range(1,len(N[0])):
            H[i][j]+=H[i][j-1]
    W=[[0, None ] for _ in range(t)]
    W[0][1]=[ 0 for _ in range(len(N))]
    max_id=0
    for i in range(len(N)):
        if W[0][0]<N[i][0]:
            W[0][0]=N[i][0]
            max_id=i
    W[0][1][max_id]=1
    for i in range(1,t):
        for j in range(i):
            for k in range(len(N)):
                if W[j][1][k]+i-j < len(H[0]):
                    q = W[j][0]
                    q+=H[k][ W[j][1][k] + i-j-1]
                    if W[j][1][k]!=0:
                        q-=H[k][ W[j][1][k] ]
                    if W[i][0] < q:
                        W[i][0] = q
                        W[i][1] = W[j][1].copy()
                        W[i][1][k]+=(i-j)
    for el in H:
        print(el)
    print()
    for el in W:
        print(el)

    return W[t-1][0]

t=4
N=[
    [4,5,3,7,1],
    [3,6,2,1,12],
    [4,6,6,1,2],
    [5,6,2,1,4],
    [1,1,12,1,2]
]

print(f(N, t))
'''
'''
def rek(T, ruchy, x, y, W):
    if x<0 or x>=len(T) or y<0 or y>=len(T) or W[x][y] is False:
        return False
    if x==len(T)-1 and y==len(T)-1:
        return True
    W[x][y]=False
    q=(rek(T, ruchy, x+ruchy[0][0], y+ruchy[0][1], W) or rek(T, ruchy, x+ruchy[1][0], y+ruchy[1][1], W) or rek(T, ruchy, x+ruchy[2][0], y+ruchy[2][1], W) or rek(T, ruchy, x+ruchy[3][0], y+ruchy[3][1], W))
    return q

def f(T, k):
    ruchy=((1,0), (-1,0), (0,-1), (0,1))
    W=[[True if T[i][j]>k else False for j in range(len(T[i]))] for i in range(len(T))]
    q=rek(T, ruchy, 0, 0, W)
    for row in W:
        print(row)
    return q

T=[
    [2,2,2,0,2],
    [2,0,2,0,2],
    [2,2,0,2,0],
    [2,2,2,2,0],
    [2,0,2,2,2]
]
k=1
print(f(T, k))
'''
'''
import random

def partition(T, l, p):
    a=random.randint(l, p)
    pivot=T[a][1]
    T[a], T[p] = T[p], T[a]
    j=l
    for i in range(l, p):
        if(T[i][1]<=pivot):
            T[i], T[j] = T[j], T[i]
            j+=1
    T[p], T[j] = T[j], T[p]
    return j

def quicksort(T, l, p): #rekurencyjnie
    while l<p:
        q=partition(T, l, p)
        if abs(q-1-l)<abs(p-q+1):
            quicksort(T, l, q-1)
            l=q+1
        else:
            quicksort(T, q+1, p)
            p=q-1

def select_buildings(W, p): #zrobione bez przeindeksowania bo mi sie nie chce
    F=[[-1 for j in range(p+1)] for i in range(len(T))]
    Profit=[T[i][0]*(T[i][2]-T[i][1]) for i in range(len(T))]
    Prev=[[None for j in range(p+1)] for i in range(len(T))]
    quicksort(T, 0, len(T)-1) #po x
    F[0][T[0][3]]=Profit[0]
    maks=-1
    maks_id=None
    for i in range(1,len(T)):
        for j in range(i):
            if T[i][1]>=T[j][2]:
                for k in range(T[i][3], p+1):
                    if F[i][k]<F[j][k-T[i][3]]+Profit[i]:
                        F[i][k]=F[j][k-T[i][3]]+Profit[i]
                        Prev[i][k]=j
                        if maks<F[i][k]:
                            maks=F[i][k]
                            maks_id=(i, k)
                        elif maks==F[i][k] and maks_id[1]>k:
                            maks_id=(i, k)
    v=maks_id[0]
    Path=[]
    while v is not None:
        Path.append(v)
        v=Prev[v][maks_id[1]]
    return Path[::-1]

T=[
    (2, 1, 5, 3),
    (3, 7, 9, 2),
    (2, 8, 11, 1)
]
p=5

print(select_buildings(T, p))
'''
'''
from math import inf
from queue import PriorityQueue

class Vertex:
    def __init__(self, id, Edges, CPN, Dist, Processed):
        self.id=id
        self.Edges=Edges
        self.CPN=CPN
        self.Dist=Dist
        self.Processed=Processed

class PQ_el:
    def __init__(self, val, id, f): #w sumie nie id tylko wierzcholek
        self.val=val
        self.id=id
        self.f=f
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

def jak_dojade(G, P, d, s, t):
    Vertices=[Vertex(i, None, False, [inf for _ in range(d+1)], [False for _ in range(d+1)]) for i in range(len(G))]
    for i in range(len(G)):
        Vertices[i].Edges=[ Vertices[j] for j in range(len(G)) if G[i][j]!=-1 ]
    for st in P:
        Vertices[st].CPN=True
    Vertices[s].Dist[d]=0
    pq=PriorityQueue((d+1)*(len(G)**2))
    pqel=PQ_el(0, Vertices[s], d)
    pq.put(pqel)
    while pq.empty() is False: #TODO: warunek
        new=pq.get()
        v, f = new.id, new.f
        if v.Processed[f] is False:
            for edge in v.Edges:
                if G[v.id][edge.id]<=f:
                    if edge.CPN is True:
                        if edge.Dist[d]>v.Dist[f]+G[v.id][edge.id]:
                            edge.Dist[d]=v.Dist[f]+G[v.id][edge.id]
                            pqel=PQ_el(v.Dist[f]+G[v.id][edge.id], edge, d)
                            pq.put(pqel)
                    else:
                        if edge.Dist[f-G[v.id][edge.id]]>v.Dist[f]+G[v.id][edge.id]:
                            edge.Dist[f-G[v.id][edge.id]]=v.Dist[f]+G[v.id][edge.id]
                            pqel=PQ_el(v.Dist[f]+G[v.id][edge.id], edge, f-G[v.id][edge.id])
                            pq.put(pqel)
        v.Processed[f]=True
    for dist in Vertices[t].Dist:
        print(dist)
    return

G = [[-1, 6,-1, 5, 2],
[-1,-1, 1, 2,-1],
[-1,-1,-1,-1,-1],
[-1,-1, 4,-1,-1],
[-1,-1, 8,-1,-1]]

P = [0,1,3]

print("A")
jak_dojade(G, P, 5, 0, 2)
print("B")
jak_dojade(G, P, 6, 0, 2)
print("C")
jak_dojade(G, P, 3, 0, 2)
'''

'''
from math import inf
from queue import PriorityQueue

class Vertex:
    def __init__(self, id, Edges, Weights):
        self.id=id
        self.Edges=Edges
        self.Weights=Weights

class PQ:
    def __init__(self, val, vtx, info):
        self.val=val
        self.vtx=vtx
        self.info=info
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

def Dijkstra(v, n, L, w):
    pq=PriorityQueue(n**2)
    Dists=[inf for _ in range(n)]
    Proc=[False for _ in range(n)]
    Prev=[None for _ in range(n)]
    Dists[v.id]=0
    pq.put(PQ(0, v, 1))
    while pq.empty() is False:
        a=pq.get()
        dist, v, i = a.val, a.vtx, a.info
        if i==len(w):
            return dist, Prev, v.id
        if Proc[v.id] is False:
            for j in range(len(v.Edges)):
                if L[v.Edges[j].id]==w[i]:
                    if dist+v.Weights[j]<Dists[v.Edges[j].id]:
                        Prev[v.Edges[j].id]=v.id
                        Dists[v.Edges[j].id]=dist+v.Weights[j]
                        pq.put(PQ(Dists[v.Edges[j].id], v.Edges[j], i+1))
        Proc[v.id]=True
    return inf, [], -1

def letters(G, w):
    L, E = G
    Vertices=[Vertex(i, [], []) for i in range(len(L))]
    for edge in E:
        u, v, wg = edge
        Vertices[u].Edges.append(Vertices[v])
        Vertices[u].Weights.append(wg)
        Vertices[v].Edges.append(Vertices[u])
        Vertices[v].Weights.append(wg)
    minimum=inf
    start=-1
    for i in range(len(Vertices)):
        if L[i]==w[0]:
            a, b, c = Dijkstra(Vertices[i], len(L), L, w)
            if a<minimum:
                Prevy=b
                start=c
    Res=[]
    if start>=0:
        while Prevy[start] is not None:
            Res.append(start)
            start=Prevy[start]
        Res.append(start)
    return Res[::-1]

L = ["k","k","o","o","t","t"]
E = [(0,2,2), (1,2,1), (1,4,3), (1,3,2), (2,4,5), (3,4,1), (3,5,3) ]
G = (L,E)
w="kto"
print(letters(G, w))
'''
'''
from math import inf
from queue import PriorityQueue

class Vertex:
    def __init__(self, id, Edges, Weights, dist, proc):
        self.id=id
        self.Edges=Edges
        self.Weights=Weights
        self.dist=dist
        self.proc=proc
    def __gt__(self, other):
        return self.dist>other.dist
    def __ge__(self, other):
        return self.dist>=other.dist
    def __eq__(self, other):
        return self.dist==other.dist
    def __lt__(self, other):
        return self.dist<other.dist
    def __le__(self, other):
        return self.dist<=other.dist

def Dijkstra(s, t, T):
    pq=PriorityQueue(len(T)**2)
    pq.put(s)
    s.dist=0
    while pq.empty() is False:
        v=pq.get()
        if v==t:
            return v.dist
        if v.proc is False:
            for i in range(len(v.Edges)):
                if v.Edges[i].dist>v.dist+v.Weights[i]:
                    v.Edges[i].dist=v.dist+v.Weights[i]
                    pq.put(v.Edges[i])
        v.proc=True
    return -1

def f(T):
    Vertices=[Vertex(i, [], [], inf, False) for i in range(len(T))]
    W=[[0 for i in range(10)] for j in range(len(T))]
    minimum=inf
    min_id=-1
    maksimum=-1
    max_id=-1
    for i in range(len(T)):
        n=T[i]
        if n>maksimum:
            maksimum=n
            max_id=i
        if n<minimum:
            minimum=n
            min_id=i
        while n>=10:
            a=n%10
            n//=10
            W[i][a]+=1
        W[i][n]+=1
        print(T[i], W[i])
    for i in range(len(T)):
        for j in range(len(T)):
            for cyfra in range(10):
                if i!=j and W[i][cyfra]>0 and W[j][cyfra]>0:
                    Vertices[i].Edges.append(Vertices[j])
                    Vertices[i].Weights.append(abs(T[i]-T[j]))
                    Vertices[j].Edges.append(Vertices[i])
                    Vertices[j].Weights.append(abs(T[i]-T[j]))
    return Dijkstra(Vertices[min_id], Vertices[max_id], T)

T = [123,890,688,587,257,246]
print(f(T))
'''
'''
from math import inf
from queue import PriorityQueue

class Vertex:
    def __init__(self, dist1, dist2, Edges, Weights, proc):
        self.dist1=dist1
        self.dist2=dist2
        self.Edges=Edges
        self.Weights=Weights
        self.proc=proc

class PQ:
    def __init__(self, dist, vtx, prev):
        self.dist=dist
        self.vtx=vtx
        self.prev=prev
    def __gt__(self, other):
        return self.dist>other.dist
    def __ge__(self, other):
        return self.dist>=other.dist
    def __eq__(self, other):
        return self.dist==other.dist
    def __lt__(self, other):
        return self.dist<other.dist
    def __le__(self, other):
        return self.dist<=other.dist

def Dijkstra(x, y):
    x.dist1, x.dist2 = 0, 0
    pq=PriorityQueue(len(G)**2)
    pq.put(PQ(0, x, 1))
    pq.put(PQ(0, x, 2))
    while y.proc is False and pq.empty() is False:
        el=pq.get()
        dist, v, prev = el.dist, el.vtx, el.prev
        if v.proc is False:
            if prev==1:
                for i in range(len(v.Edges)):
                    if v.Edges[i].dist2>dist+v.Weights[i]:
                        v.Edges[i].dist2=dist+v.Weights[i]
                        v.Edges[i].dist1=min(v.dist1, v.Edges[i].dist1)
                        pq.put(PQ(v.Edges[i].dist1, v.Edges[i], 2)) #
            else:
                for i in range(len(v.Edges)):
                    if v.Edges[i].dist1>dist+v.Weights[i]:
                        v.Edges[i].dist1=dist+v.Weights[i]
                        v.Edges[i].dist2=min(v.dist2, v.Edges[i].dist2)
                        pq.put(PQ(v.Edges[i].dist2, v.Edges[i], 1)) #
        v.proc=True
    return

def f(G, x, y):
    V=[Vertex(inf, inf, [], [], False) for _ in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j]!=0 and i<j:
                V[i].Edges.append(V[j])
                V[j].Edges.append(V[i])
                V[i].Weights.append(G[i][j])
                V[j].Weights.append(G[i][j])
    Dijkstra(V[x], V[y])
    return min(V[y].dist1, V[y].dist2)

G=[
    [0,10,0,0,90],
    [10,0,200,0,0],
    [0,200,0,20,0],
    [0,0,20,0,80],
    [90,0,0,80,0]
]

print(f(G, 0, 3))
'''
'''
from math import inf

def f(G, s, k):
    Dist=[[G[i][j] for j in range(len(G))] for i in range(len(G))]
    Prev=[[j if G[i][j]!=inf and G[i][j]!=0 else None for j in range(len(G))] for i in range(len(G))]
    for t in range(len(G)):
        for v in range(len(G)):
            for u in range(len(G)):
                if Dist[v][t]+Dist[t][u]<Dist[v][u]:
                    Dist[v][u]=Dist[v][t]+Dist[t][u]
                    Prev[v][u]=Prev[v][t]
    print(Prev)
    print("dist:", Dist[s][k])
    stop=s
    while stop!=k:
        print(stop)
        stop=Prev[stop][k]
    print(k)

G=[
    [0, 2, inf, inf, 1],
    [inf, 0, 2, inf, inf],
    [inf, inf, 0, inf, inf],
    [inf, inf, 1, 0, inf],
    [inf, inf, inf, 1, 0]
]
G=[
    [0, 2, inf, 1, inf],
    [inf, 0, 2, inf, inf],
    [inf, inf, 0, inf, inf],
    [inf, inf, inf, 0, 1],
    [inf, inf, 1, inf, 0]
]
f(G, 0, 2)

'''
'''
from random import randint

def partition(T, l, p): #po x
    pivot=T[p][0]
    j=l
    for i in range(l, p):
        if T[i][0]<=pivot:
            T[i], T[j] = T[j], T[i]
            j+=1
    T[p], T[j] = T[j], T[p]
    return j

def quicksort(T, l, p): #rekurencyjnie
    while l<p:
        q=partition(T, l, p)
        if abs(q-1-l)<abs(p-q+1):
            quicksort(T, l, q-1)
            l=q+1
        else:
            quicksort(T, q+1, p)
            p=q-1

def dl(A):
    return A[1]-A[0]

def f(T, k):
    quicksort(T, 0, len(T)-1)
    print(T)
    Prev=[[(None, None) for j in range(k+1)] for i in range(len(T))]
    F=[[0 for j in range(k+1)] for i in range(len(T))]
    F[0][1]=dl(T[0])
    for i in range(1,len(T)):
        F[i][1]=dl(T[i])
        for l in range(k+1):
            for j in range(i):
                if F[j][l-1]!=0 and T[j][1]==T[i][0] and F[i][l]<F[j][l-1]+dl(T[i]):
                    F[i][l]=F[j][l-1]+dl(T[i])
                    Prev[i][l]=(j, l-1)
    maksimum=0
    max_id=-1
    for row in range(len(F)):
        if maksimum<F[row][k]:
            maksimum=F[row][k]
            max_id=(row, k)
    while max_id!=(None, None):
        print(max_id)
        max_id=(Prev[max_id[0]][max_id[1]][0], Prev[max_id[0]][max_id[1]][1])
    return None

T=[(1,3), (0, 2), (-2, 7), (-10, 12), (0, 5), (5, 10), (5, 7), (5, 9), (9, 12), (9, 10), (7, 9), (12, 34), (10, 13)]
f(T, 3)
'''
'''
from math import inf

def partition(T, l, p):
    pivot=T[p]
    j=l
    for i in range(l, p):
        if T[i]<=pivot:
            T[i], T[j] = T[j], T[i]
            j+=1
    T[p], T[j] = T[j], T[p]
    return j

def quicksort(T, l, p):
    while l<p:
        q=partition(T, l, p)
        if abs(q-1-l)<abs(p-q+1):
            quicksort(T, l, q-1)
            l=q+1
        else:
            quicksort(T, q+1, p)
            p=q-1

def partition_x(T, l, p):
    pivot=T[p][0]
    j=l
    for i in range(l, p):
        if T[i][0]<=pivot:
            T[i], T[j] = T[j], T[i]
            j+=1
    T[p], T[j] = T[j], T[p]
    return j

def quicksort_x(T, l, p):
    while l<p:
        q=partition_x(T, l, p)
        if abs(q-1-l)<abs(p-q+1):
            quicksort_x(T, l, q-1)
            l=q+1
        else:
            quicksort_x(T, q+1, p)
            p=q-1

def partition_y(T, l, p):
    pivot=T[p][1]
    j=l
    for i in range(l, p):
        if T[i][1]<=pivot:
            T[i], T[j] = T[j], T[i]
            j+=1
    T[p], T[j] = T[j], T[p]
    return j

def quicksort_y(T, l, p):
    while l<p:
        q=partition_y(T, l, p)
        if abs(q-1-l)<abs(p-q+1):
            quicksort_y(T, l, q-1)
            l=q+1
        else:
            quicksort_y(T, q+1, p)
            p=q-1

def overlapping(a, b):
    a1, a2, b1, b2 = a[0], a[1], b[0], b[1]
    if a1==b1:
        return None
    if b1<=a2:
        return True
    return False

def f(T, a, b):
    H=[]
    for i in range(len(T)):    
        if T[i][0] not in H and T[i][0]:
            H.append(T[i][0])
        if T[i][1] not in H and T[i][1]:
            H.append(T[i][1])
    quicksort(H, 0, len(H)-1)
    quicksort_y(T, 0, len(T)-1)
    quicksort_x(T, 0, len(T)-1)
    F=[inf for i in range(len(T))]
    start=0
    while start<len(T) and T[start][1]<a:
        start+=1
    F[start]=1
    for i in range(start+1, len(T)):
        for j in range(start, i):
            if overlapping(T[j], T[i]) is None:
                F[i]=min(F[i], F[j])
            elif overlapping(T[j], T[i]) is True:
                F[i]=min(F[i], 1+F[j])
    minimum=inf
    for i in range(len(T)):
        if T[i][1]>=b:
            minimum=min(minimum, F[i])
    return minimum


T1 = [(0,5),(1,6),(2,7),(3,8),(4,9),(5,10)]
print(f(T1, 0, 10))
'''
'''
from math import inf
from random import randint
import copy, collections
    
class interval_tree:
    def __init__(self, val, left, right, a, b, intervals, number):
        self.val=val
        self.left=left
        self.right=right
        self.a=a
        self.b=b
        self.intervals=intervals
        self.number=number

def bfs(graph, s, t, parent):
    visited = [False] * len(graph)
    queue = collections.deque()
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.popleft()
        for ind, val in enumerate(graph[u]):
            if (visited[ind] == False) and (val > 0):
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
    return visited[t]

def edmonds_karp(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0
    while bfs(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow

def in_order(root):
    if root.left is not None:
        in_order(root.left)
    print(root.val)
    if root.right is not None:
        in_order(root.right)

def left(parent, T, l, p):
    q=(l+p)//2
    if p-l==1:
        return interval_tree(T[q], None, None, parent.a, parent.val, [], 0)
    elif p==l:
        return None
    q=(l+p)//2
    new=interval_tree(T[q], None, None, parent.a, parent.val, [], 0)
    k, r = left(new, T, l, q), right(new, T, q+1, p)
    new.left=k
    new.right=r
    return new

def right(parent, T, l, p):
    q=(l+p)//2
    if p-l==1:
        return interval_tree(T[q], None, None, parent.val, parent.b, [], 0)
    elif p==l:
        return None
    new=interval_tree(T[q], None, None, parent.val, parent.b, [], 0)
    k, r = left(new, T, l, q), right(new, T, q+1, p)
    new.left=k
    new.right=r
    return new

def insert(root, l, p, id):
    if root is None:
        return
    if root.a==l and root.b==p:
        root.number+=1
        root.intervals.append((id, l, p))
    elif p<root.val:
        insert(root.left, l, p, id)
    elif l>root.val:
        insert(root.right, l, p, id)
    else:
        insert(root.left, l, root.val, id)
        insert(root.right, root.val, p, id)

def finish(root):
    if root.left is not None:
        finish(root.left)
    else:
        new=interval_tree((root.a+root.val)/2, None, None, root.a, root.val, [], 0)
        root.left=new
    if root.right is not None:
        finish(root.right)
    else:
        new=interval_tree((root.val+root.b)/2, None, None, root.val, root.b, [], 0)
        root.right=new

def lets_make_a_graph(root, l, p, G):
    if root is None:
        return
    if root.a==l and root.b==p:
        G.append([el[0] for el in root.intervals])
    elif p<root.val:
        lets_make_a_graph(root.left, l, p, G)
    elif l>root.val:
        lets_make_a_graph(root.right, l, p, G)
    else:
        lets_make_a_graph(root.left, l, root.val, G)
        lets_make_a_graph(root.right, root.val, p, G)

def make_tree(T, I, a, b):
    q=len(T)//2
    root=interval_tree(T[q], None, None, -inf, inf, [], 0)
    l, p = left(root, T, 0, q), right(root, T, q+1, len(T))
    root.left=l
    root.right=p
    finish(root)
    #in_order(root)
    #print(root.val)
    #print(root.left.val, root.right.val)
    #print(root.left.left.val, root.left.right.val, root.right.left.val, root.right.right.val)
    for i in range(len(I)):
        insert(root, I[i][0], I[i][1], i)
    G=[]
    lets_make_a_graph(root, a, b, G)
    Count=[0 for _ in range(len(T))]
    Index=[-1 for _ in range(len(T))]
    licznik=0
    for row in G:
        for el in row:
            if Count[el]==0:
                Count[el]=1
                Index[licznik]=el
                licznik+=1
            else:
                Count[el]+=1
    M=[[0 for j in range(2+len(G)+licznik)] for i in range(2+len(G)+licznik)]
    for i in range(licznik):
        for j in range(len(G)):
            if Index[i] in G[j]:
                M[i][licznik+j]=1
    for i in range(len(G)):
        M[licznik+i][len(M)-1]=1
    j=0
    for i in range(len(Count)):
        if Count[i]>0:
            j+=1
            M[len(M)-2][j]=Count[i]
    print(edmonds_karp(M, len(M)-2, len(M)-1))
    #nie daje odpowiedzi na pytanie o minimum ale daje odpowiedz czy da sie przejsc

T=[0, 1, 2, 3, 4, 5, 7, 10]
I=[(0,4),(1,5),(0,2),(3,7),(7,10)]
a, b = 0, 10
    
make_tree(T, I, a, b)
'''