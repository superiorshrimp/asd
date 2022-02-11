'''
Zad. 1. Dane są dwie tablice int t1[N], int t2[N] wypełnione liczbami naturalnymi. Proszę napisać funkcję, która
sprawdza czy z każdej z tablic można wyciąć po jednym kawałku, tak aby suma elementów w obu kawałkach była:
co najmniej drugą potęgą dowolnej liczby naturalnej. Łączna długości obu kawałków powinna wynosić 24
'''
'''
import random
N=10
T1=[random.randint(1, 10) for i in range(N)]
T2=[random.randint(1, 10) for i in range(N)]

def czy_druga_potega(n):
    s=0
    i=1
    while(s<n):
        s+=i
        i+=2
    if(s==n):
        return True
    return False

for i in range(N):
    s=T1[i]
    p=1
    while(s<24):
        s+=T1[i+p]
        
        p+=1
'''
'''
Zad. 1. Dane są dwie tablice int t1[N], int t2[N] wypełnione liczbami naturalnymi. Proszę napisać funkcję, która
sprawdza czy z każdej z tablic można wyciąć po jednym kawałku, tak aby suma elementów w obu kawałkach była:
iloczynem dokładnie dwóch liczb pierwszych. Oba kawałki powinny być jednakowej długości.
'''
'''
import random
N=10
T1=[random.randint(1, 10) for i in range(N)]
T2=[random.randint(1, 10) for i in range(N)]

def suma(T):
    s=0
    for k in T:
        s+=k
    print(s)
    return s

def F(T1, T2, N):
    for i in range(N):
        for j in range(N):
            T1C=[T1[l] for l in range(N)]
            T2C=[T2[l] for l in range(N)]
            p=0
            while(i+p+1<N and j+p+1<N):
                del T1C[i]
                del T2C[j]
                p+=1
                if(suma(T1C)==suma(T2C)):
                    return True
    return False


if(F(T1, T2, N)==True):
    print("da sie")
else:
    print("nie da sie")
'''
'''
N=1000
Tablica tab jest wypeªniona liczbami naturalnymi. Prosz¦ napisa¢ funkcj¦, która zwraca dªugo±¢ najdªu»szego
spójnego podci¡gu rosn¡cego, dla którego suma jego elementów jest równa sumie indeksów tych elementów.
Do funkcji nale»y przekaza¢ tablic¦, funkcja powinna zwróci¢ dªugo±¢ znalezionego podci¡gu, lub warto±¢ 0,
je»eli taki podci¡g nie istnieje.
'''
'''
import random
N=1000
T=[random.randint(1, 1000) for i in range(N)]

def f(T, N):
    max=0
    for i in range(N):
        s=0
        si=0
        p=1
        while(i+p<N and T[i+p]>T[i+p-1]):
            s+=T[i+p]
            si+=i+p
            p+=1
            if(si==s and p>max):
                max=p
    return max


print(f(T, N))
'''
'''
Zadanie 3.
Dwie listy zawieraj¡ niepowtarzaj¡ce si¦ (w obr¦bie listy) liczby naturalne. W obu listach liczby s¡ posortowane rosn¡co. Prosz¦ napisa¢ funkcj¦ usuwaj¡c¡ z ka»dej listy liczby wyst¦puj¡ce w drugiej. Do funkcji
nale»y przekaza¢ wskazania na obie listy, funkcja powinna zwróci¢ ª¡czn¡ list¦ usuni¦tych elementów.
'''
'''
import random
N=100
T1=[]
T2=[]
for i in range(N):
    a=random.randint(1, 1000)
    while a in T1:
        a=random.randint(1, 1000)
    T1.append(a)
for i in range(N):
    a=random.randint(1, 1000)
    while a in T2:
        a=random.randint(1, 1000)
    T2.append(a)
T1.sort()
T2.sort()
def f(T1, T2, N):
    p=0
    l=0
    D=[]
    while(l<N and p<N):
        if(T1[l]==T2[p]):
            D.append(T1[l])
            T1[l], T2[p] = 0, 0
            l+=1
            p+=1
        elif(T1[l]>T2[p]):
            p+=1
        else:
            l+=1
    T1=list(set(T1))
    T1.sort()
    T1.remove(0)
    T2=list(set(T2))
    T2.sort()
    T2.remove(0)
    return T1, T2, D
            
T1, T2, D=f(T1, T2, N)
print(T1[:], T2[:], D[:])
print(len(D))
'''
'''
Ład. L Dana jest tablica int t[N][N] zawierająca liczby naturalne. Dokładnie w jednym z wierszy
tablicy znajduje się fragment ciągu Fibonacciego o długościwiększej niż2,a mniejszej niż N. Proszę
napisać funkcję, która odszuka ten fragment ciągu i zwróci numer wiersza w którym on się znajduje.
'''
'''
import random

def fib():
    F=[]
    a=1
    b=1
    while(a<100_000):
        F.append(a)
        a, b = a+b, a
    return F

N=10
T=[[random.randint(1, 100_000) for j in range(N)] for i in range(N)]
T[7][3]=34
T[7][4]=55
T[7][5]=89
T[7][6]=144
F=fib()
#print(T[7][:])
def f(T, F):
    max=0
    maxi=999
    N=len(T)
    for i in range(N):
        for j in range(N-2):
            if T[i][j] in F:
                licznik=1
                for k in range(len(F)):
                    if(F[k]==T[i][j]):
                        break
                p=1
                while(j+p<N):
                    if(F[k+p]==T[i][j+p]):
                        licznik+=1
                        if(licznik>max):
                            max=licznik
                            maxi=i
                    p+=1
    return max, maxi

print(f(T, F))
'''
'''
Zadanie 2.
Tablica t[N] jest wypełniona liczbami naturalnymi. Skok z pola i-tego można
wykonać na pola o indeksach i+k, gdzie k jest czynnikiem pierwszym liczby
t[i] (mniejszym od niej samej). Napisz funkcję, która sprawdza, czy da się
przejść z pola 0 do N-1 – jeśli się da, zwraca ilość skoków, jeśli się nie da,
zwraca -1
'''
'''
import random
N=100
T=[random.randint(2, 100) for i in range(N)]

def pierwsze(n):
    D=[]
    for i in range(2, int(n**(0.5))+1):
        if(n%i==0):
            D.append(i)
            n//=i
            while(n%i==0):
                n//=i
            i+=1
    if(len(D)==0):
        return [N]
    return D


def rek(T, N, k):
    D=pierwsze(T[k])
    for l in D:
        k+=l
        if(k==N-1):
            return True
        while(k<N):
            rek(T, N, k)
        if(k>N):
            return False
    return False

k=0
T=[15, 2, 7, 4, 5, 6]
N=6
D=pierwsze(T[k])
for l in D:
    k=0
    k+=l
    if(True==rek(T, N, k)):
        print("tak")
        exit(0)
print("nie")
'''
'''
2. Proszę napisać program, który wypełnia tablicę int tab[MAX] trzycyfrowymi liczbami
pseudolosowymi, a następnie wyznacza i wypisuje długość najdłuższego podciągu spójnego
znajdującego się w tablicy dla którego w tablicy występuje również rewers tego ciągu.
Na przykład dla tablicy: 2,9,3,1,7,11,9,6,7,7,1,3,9,12,15 odpowiedzią jest liczba 4.
'''
'''
import random
#N=100
#T=[int(str(random.randint(1, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))) for i in range(N)]

T=[2,9,3,1,7,11,9,6,7,7,1,3,9,12,15]
N=len(T)
max=0

for i in range(N-1):
    l=N-1
    while(l>0):
        if(T[i]==T[l]):
            p=1
            while(i+p<N and l-p>0):
                if(T[i+p]!=T[l-p]):
                    break
                if(p>max):
                    max=p+1
                p+=1
        l-=1
print(max)
'''
'''
1. Dana jest liczba naturalna N niezawierająca cyfry 0, którą rozbijamy na dwie liczby naturalne
A i B, przenosząc kolejne cyfry z liczby N do liczby A albo B. Na przykład liczbę 21523
możemy rozbić na wiele sposobów, np. (215,23),(2,1523),(223,15),(152,23),(22,153),(1,2523)...
Uwaga: względna kolejność cyfr w liczbie N oraz liczbach A i B musi być zachowana. Proszę
napisać funkcję generującą i wypisującą wszystkie rozbicia, w których powstałe liczby A i B
są względnie pierwsze. Do funkcji należy przekazać wartość N, funkcja powinna zwrócić liczbę
znalezionych par.
Uwagi:
- warunek względnej pierwszości można pominąć kosztem 1 pkt
- do funkcji można przekazać dodatkowe parametry
- czas na rozwiązanie obu zadań wynosi 45 minut
- za każde zadanie można otrzymać maksymalnie 5 pkt
- oceniane będą: czytelność, poprawność i efektywność rozwiązań
'''
'''
N="6543762"

def czy_wzglednie_pierwsze(a, b):
    while(b!=0):
            b, a = a%b, b
    if(a==1):
        return True
    return False

licznik=0

for i in range(1, len(N)):
    for j in range(len(N)-i+1):
        a=""
        b=""
        p=0
        P=[]
        while(p<i):
            a+=N[j+p]
            P.append(j+p)
            p+=1
        for k in range(len(N)):
            if k not in P:
                b+=N[k]
        if(czy_wzglednie_pierwsze(int(a), int(b))==True):
            licznik+=1
            print(a, b)

#powtarzaja sie wyniki
'''
'''
1. Dwie liczby naturalne są „koleżankami” jeżeli mają przynajmniej dwie różne wspólne cyfry,
np. 123 i 1345 lub 225 i 1235. Dana jest tablica t[N][N] wypełniona liczbami naturalnymi.
Proszę napisać funkcję, która w tablicy t zeruje wszystkie liczby nie mające żadnej koleżanki.
Do funkcji należy przekazać tablicę t. Funkcja powinna zwrócić ilość liczb naturalnych jaka
pozostanie w tablicy.
Uwagi:
- czas na rozwiązanie obu zadań wynosi 45 minut
- za każde zadanie można otrzymać maksymalnie 5 pkt
- oceniane będą: czytelność, poprawność i efektywność rozwiązań
'''
'''
import random
N=10
T=[[random.randint(100, 99999) for j in range(N)] for i in range(N)]

def wsp_cyfry(a, b):
    licznik=0
    for l in a:
        if l in b:
            licznik+=1
        if(licznik>2):
            return True
    return False

def podzial(n):
    w=""
    while(n>=10):
        if str(n%10) not in w:
            w+=str(n%10)
        n//=10
    return w

def f(T, N):
    licznik=0
    for i in range(N):
        for j in range(N):
            if(T[i][j]>0):
                T[i][j]=podzial(T[i][j])
                pom=0
                for k in range(i, N):
                    if(k==i):
                        for l in range(j+1, N):
                            if(wsp_cyfry(T[i][j], podzial(T[k][l]))==True):
                                T[i][j]*=-1
                                T[k][l]*=-1
                                licznik+=1
                                pom=1
                                break
                    else:
                        for l in range(N):
                            if(wsp_cyfry(T[i][j], podzial(T[k][l]))==True):
                                T[i][j]*=-1*int(T[i][j])
                                T[k][l]*=-1*int(T[k][l])
                                licznik+=1
                                break
                    if(pom==1):
                        break
                if(pom==0):
                    T[i][j]=0
        return T, licznik
#...

print(f(T, N))
'''
'''
Zadanie 5. Dana jest liczba naturalna o niepowtarzających się cyfrach pośród których nie ma zera. Ile
różnych liczb podzielnych np. przez 7 można otrzymać poprzez wykreślenie dowolnych cyfr w tej liczbie. Np.
dla 2315 będą to 21, 35, 231, 315
'''
#wrocic
'''
Zadanie 14. Dwie liczby naturalne są zgodne jeżeli w zapisie dwójkowym zawierają tę samą liczbę jedynek,
np. 22 = 101102 i 14 = 11102. Dane są tablice T1[N1][N1] T2[N2][N2], gdzie N2¿N1. Proszę napisać funkcję,
która sprawdza czy istnieje takie położenie tablicy T1 wewnątrz tablicy T2, przy którym liczba zgodnych
elementów jest większa od 33%. Do funkcji należy przekazać tablicę T1 i T2. Obie oryginalne tablice powinny
pozostać nie zmieniane.
'''
'''
import random

def zamiana_na_binarny(n):
    w=0
    while(n!=0):
        w+=1
        n//=2
    return w

T1=[[random.randint(1, 100) for j in range(25)] for i in range(25)]
T2=[[random.randint(1, 100) for j in range(10)] for i in range(10)]

def f(T1, T2):
    pole=len(T2)**2
    for i in range(len(T1)-len(T2)+1):
        for j in range(len(T1)-len(T2)+1):
            licznik=0
            for k in range(len(T2)):
                for l in range(len(T2)):
                    if(zamiana_na_binarny(T1[i][j])==zamiana_na_binarny(T2[k][l])):
                        licznik+=1
            if(licznik/pole>1/3):
                return True
    return False

print(f(T1, T2))
'''
'''
def rek(T, i, p, licznik, max):
    for j in range(len(T)):
        TC=[T[o] for o in range(len(T))]
        if(j!=i+p and j!=i and T[j]>0):
            if(T[j]==T[i+p]):
                licznik+=1  
                TC[i+p], TC[i]=-2*licznik, -2*licznik-1 
                i=j
                if(i%2==0):
                    p=1
                else:
                    p=-1
                i=i+p
                if(licznik>max):
                    max=licznik
                return rek(TC, i, p, licznik, max)
    return max

def f(T):
    max=0
    for i in range(len(T)):
        licznik=0
        if(i%2==0):
            p=1
        else:
            p=-1
        for j in range(len(T)):
            TC=[T[o] for o in range(len(T))]
            if(j!=i+p and j!=i):
                if(T[j]==T[i+p]):
                    licznik+=1  
                    TC[i+p], TC[i]=-2*licznik, -2*licznik-1 
                    i=j
                    if(i%2==0):
                        p=1
                    else:
                        p=-1
                    if(licznik>max):
                        max=licznik
                    return rek(TC, i, p, licznik, max)
T=[1,3,3,4,5,4,6,4]
print(f(T))
#zle
'''
'''
#14:39
def rek(T, TP, i, licznik):
    for j in range(len(T)):
        if(T[i][1]==T[j][0]):
            TP[licznik]=(T[i][0], T[i][1])
            licznik+=1
            if(licznik==len(T)):
                return TP
            if(rek(T, TP, j, licznik)==0)
                pass
            else:
                return rek(T, TP, j, licznik)
    return 0

def f(T):
    for i in range(len(T)):
        TP=[0]*len(T)
        licznik=1
        for j in range(len(T)):
            if(T[i][1]==T[j][0]):
                TP[licznik]=(T[i][0], T[i][1])
                licznik+=1
                if(rek(T, TP, j, licznik)!=0):
                    return rek(T, TP, j, licznik)

T=[(2,9),(3,6),(8,2),(2,3),(6,2)]

print(f(T))
#nie wiem czemu nie dziala
'''
'''
Zadanie 1.
Dana jest tablica int t[N] wypeªniona liczbami caªkowitymi. Prosz¦ napisa¢ funkcj¦, która sprawdza, czy
mo»liwe jest "poci¦cie" tablicy na co najmniej 2 kawaªki o jednakowych sumach elementów. Do funkcji nale»y
przekaza¢ tablic¦, funkcja powinna zwróci¢ najwi¦ksz¡ liczb¦ kawaªków, na któr¡ mo»na poci¡¢ tablic¦, lub
warto±¢ 0, je±li takie poci¦cie nie jest mo»liwe. Na przykªad: dla tablicy [1,2,3,1,5,2,2,2,6] odpowiedzi¡
powinno by¢ 4, bo [1,2,3|1,5|2,2,2|6].
'''
'''
def rek(T, pocz, s, k):
    for dl in range(len(T)-pocz+1):
        s1=0
        pom=0
        while(pom<dl):
            s1+=T[pocz+pom]
            pom+=1
        if(s1==s):
            k+=1
            if(pocz+pom==len(T)):
                return k
            return rek(T, pocz+pom, s1, k)
        if(s1>s):
            break
    return 0

def f(T):
    for dl in range(1, len(T)-1):
        pom=0
        s=0
        k=1
        while(pom<dl):
            s+=T[pom]
            pom+=1
        if(rek(T, pom, s, k)!=0):
            return rek(T, pom, s, k)
    return 0

T=[1,2,3,1,5,2,2,2,6]

print(f(T))
#dziala
'''
'''
Zadanie 3.
Dwie listy zawieraj¡ niepowtarzaj¡ce si¦ (w obr¦bie listy) liczby naturalne. W obu listach liczby s¡ posortowane rosn¡co. Prosz¦ napisa¢ funkcj¦ usuwaj¡c¡ z ka»dej listy liczby wyst¦puj¡ce w drugiej. Do funkcji
nale»y przekaza¢ wskazania na obie listy, funkcja powinna zwróci¢ ª¡czn¡ list¦ usuni¦tych elementów.
'''
'''
t1=[1,3,6,7,9,14,16,18]
t2=[1,4,6,9,25]
def f(t1, t2):
    u=[]
    l, p = 0, 0
    while(l<len(t1) and p<len(t2)):
        if(t1[l]==t2[p]):
            u.append(t1[l])
            l+=1
            p+=1
        if(t1[l]>t2[p]):
            p+=1
        else:
            l+=1
    print(u)
f(t1, t2)
'''
'''
Dana jest tablica int t[N][N] zawierająca liczby naturalne. Dokładnie w jednym
wierszu, bądź kolumnie znajduje się fragmentu ciągu arytmetycznego o długości
większej niż 2, którego elementy są liczbami pierwszymi. Proszę napisać funkcję
która zwróci długość tego ciągu.
'''
'''
import random
N=100
T=[[random.randint(1, 100) for j in range(N)] for i in range(N)]

def czy_pierwsza(n):
    for i in range(2, int(n**(0.5)+1)):
        if(n%i==0):
            return False
    return True

def f(T):
    max=0
    for i in range(len(T)):
        for j in range(len(T)-1):
            p=1
            if(czy_pierwsza(T[i][j])==True and czy_pierwsza(T[i][j+p])==True):
                r=T[i][j+p]-T[i][j]
                p+=1
                while(j+p<len(T)):
                    if(r==T[i][j+p]-T[i][j+p-1] and czy_pierwsza(T[i][j+p])==True):
                        p+=1
                        if(p>max):
                            max+=1
                    else:
                        break
    for j in range(len(T)):
        for i in range(len(T)-1):
            p=1
            if(czy_pierwsza(T[i][j])==True and czy_pierwsza(T[i+p][j])==True):
                r=T[i+p][j]-T[i][j]
                p+=1
                while(i+p<len(T)):
                    if(r==T[i+p][j]-T[i+p-1][j] and czy_pierwsza(T[i+p][j])==True):
                        p+=1
                        if(p>max):
                            max+=1
                    else:
                        break
    return max

print(f(T))
'''
'''
z mojego k1 zad1
'''
'''
T=["A", "B", "A", "A", "B", "A"]
def multi(T):
    max=0
    for dlugosc in range(1, len(T)//2+1):
        for poczatek in range(len(T)-2*dlugosc+1):
            p=0
            for i in range(dlugosc):
                if(T[poczatek+i]==T[poczatek+i+dlugosc]):
                    p+=1
                if(p==dlugosc):
                    max=dlugosc
    return max

print(multi(T))
'''
'''
Zad. 2 Dana jest N elementowy zbiór liczb naturalnych w postaci tablicy int t[N]. Proszę napisać
funkcję, która zwraca informację czy jest możliwy podział zbioru na trzy zbiory tak aby w każdym z
trzech zbiorów lączna liczba jedynek w liczbach zapisanych w systemie binarnym była jednakowa. Na
przykład dla zbioru |Ż,3,5,7,I1",L3,J-6} możliwy podział to {2,L3,L6} {3,L1i {5,7l czyli w systemie
dwójkowym {10,1101,10000} {11,10LLI |1o1',11'L} - w każdym zbiorze jest 5 jedynek.
'''
'''
import random
N=1000
T=[random.randint(1, 1000) for i in range(N)]

def binarny(n):
    licznik=0
    while(n!=0):
        if(n%2==1):
            licznik+=1
        n//=2
    return licznik

def f(T):
    suma=0
    for i in range(len(T)):
        T[i]=binarny(T[i])
        suma+=binarny(T[i])
    if(suma%3==0):
        for i in range(len(T)-2):

    else:
        return False

print(f(T))
#nie umiem
'''
'''
z mojego kol zad 2
'''
'''
def tmp(n, m):
    for i in range(len(n)):
        #(T, i, maxi)
        if(n[i]==1 and m[i]==0):
            return True
        elif(n[i]==0 and m[i]==1):
            return False    


def distance(T):
    maxi=0
    mini=0
    i=0
    while(i<len(T)-1):
        if(tmp(T[i], T[i+1])==True):

    return abs(maxi-mini)
'''
'''
2. W grze mag-mino wykorzystuje się klocki, które mają kształt prostokątów, na których obydwu końcach znajduje
się liczba oczek od 0 do 9. Na każdym klocku z dwóch jego końców liczba oczek jest inna. W komplecie liczącym 90
klocków do gry występują wszystkie kombinacje oczek i każda kombinacja występuje dokładnie jeden raz. Proszę
napisać funkcję, która dla danego zbioru N klocków wyznacza najdłuższy ciąg jaki można z nich ułożyć.
Na przykład dla zbioru 8 klocków: [2|8] [0|1] [2|3] [3|6] [2|6] [2|9] [3|4] [6|7]
najdłuższy ciąg jaki można ułożyć ma długość 5 i ma postać : [8|2] [2|3] [3|6] [6|2] [2|9]
Dane opisujące zestaw:
const int N= …
struct klocek {
 int a;
 int b; // b>a
};
klocek zestaw[N];
Do funkcji należy przekazać zestaw klocków, funkcja powinna zwrócić największą długość ciągu jaki można z tego
zestawu zbudować. Wskazówka : kiedy z zestawu klocków da się zbudować ciąg?
'''
'''
#14:30
def f(T, T1, dl, ostatnia):
    global max
    if(dl==len(T)):
        return dl
    for i in range(len(T1)):
        TC=[T1[p] for p in range(len(T1))]
        a=T1[i]
        del TC[i]
        if(a[0]==ostatnia):
            f(T, TC, dl+1, a[1])
        elif(a[1]==ostatnia):
            f(T, TC, dl+1, a[0])
        else:
            if(dl>max):
                max=dl

max=0
T=[[2,8],[0,1],[2,3],[3,6],[2,6],[2,9],[3,4],[6,7]]
TP=[T[i] for i in range(len(T))]
for i in range(len(T)):
    a=TP[i]
    del TP[i]
    print(f(T, TP, 1, a[0]))
    print(f(T, TP, 1, a[1]))
    TP.insert(i, a)
print(max)
'''
'''
Dane s¡ dwie tablice int t1[N] oraz int t2[N] wypeªnione liczbami naturalnymi. Elementy z tablic t1 i t2
ª¡czymy w pary (po jednym elemencie z ka»dej tablicy) tak, aby suma wybranych elementów z tablicy t1 byªa
równa sumie wybranych elementów z tablicy t2. Prosz¦ napisa¢ funkcj¦, która zwróci maksymaln¡ liczb¦
par, jak¡ mo»na uzyska¢. Do funkcji nale»y przekaza¢ wyª¡cznie tablice t1 i t2, funkcja powinna zwróci¢
maksymaln¡ liczb¦ par.
'''
'''
#17:18
def rek(t1, t2, i, j, s1, s2):
    t1c=[t1[p] for p in range(len(t1))]
    t2c=[t2[p] for p in range(len(t1))]
    b=t2c[j]
    del t2c[j]
    if(s1==s2):
        print(i)
        return True
    if(i==len(t1)):
        return None
    for n in range(len(t1)): 
        a=t1c[n]
        del t1c[n]
        rek(t1c, t2c, i-1, j+1, s1-a, s2-b)
        t1c.insert(a, n)
    t2c.insert(b, j)

def f(t1, t2):
    s1=0
    s2=0
    for i in range(len(t1)):
        s1+=t1[i]
    for i in range(len(t1)):
        s2+=t2[i]
    rek(t1, t2, len(t1), 0, s1, s2)
#zle pewnie
'''
'''
Dana jest tablica t[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
Proszę napisać funkcję która ustawia na szachownicy dwie wieże, tak aby suma liczb na
„szachowanych” przez wieże polach była największa. Do funkcji należy przekazać tablicę,
funkcja powinna zwrócić położenie wież.
Uwagi:
- zakładamy, że wieża szachuje cały wiersz i kolumnę z wyłączeniem pola na którym stoi
- czas na rozwiązanie obu zadań wynosi 45 minut
- za każde zadanie można otrzymać maksymalnie 5 pkt
- oceniane będą: czytelność, poprawność i efektywność rozwiązań
'''
'''
#17:30
import random

def suma(T, i, j):
    sw=0
    sk=0
    for k in range(len(T)):
        if(j!=k):
            sw+=T[i][k]
    for l in range(len(T)):
        if(i!=l):
            sk+=T[l][j]
    return sw+sk   

def f(T):
    top1=0
    top1cord=[-1,-1]
    top2=0
    top2cord=[-1,-1]
    for i in range(len(T)):
        for j in range(len(T)):
            if(suma(T, i, j)>top2 and suma(T, i, j)<top1):
                top2=suma(T, i, j)
                top2cord=[i, j]
            elif(suma(T, i, j)>top1):
                top1=suma(T, i, j)
                top1cord=[i, j]
    print(top1cord, top2cord)

T=[[random.randint(1, 100) for _ in range(10)] for _ in range(10)]
for i in range(len(T)):
    print(T[i])
f(T)
'''
'''
Dane są dwie tablice t1[N] i t2[N] zawierające liczby naturalne. Z wartości w obu tablicach
możemy tworzyć sumy. „Poprawna” suma to taka, która zawiera co najmniej jeden element
(z tablicy t1 lub t2) o każdym indeksie. Na przykład dla tablic: t1 = [1,3,2,4] i t2 = [9,7,4,8]
poprawnymi sumami są na przykład 1+3+2+4, 9+7+4+8, 1+7+3+8, 1+9+7+2+4+8.
Proszę napisać funkcję generującą i wypisującą wszystkie poprawne sumy, które są liczbami
pierwszymi. Do funkcji należy przekazać dwie tablice, funkcja powinna zwrócić liczbę
znalezionych i wypisanych sum
'''
'''
#17:41
def czy_pierwsza(n):
    if(n==0 or n==1):
        return False
    for i in range(2, int(n**(0.5))):
        if(n%i==0):
            return False
    return True

def rek(t1, t2, w, s, i):
    if(i==len(t1)):
        if(czy_pierwsza(s)==True):
            print(w)
        return None
    wc=[w[j] for j in range(len(w))]
    rek(t1, t2, wc+[t1[i]], s+t1[i], i+1)
    wc=[w[j] for j in range(len(w))]
    rek(t1, t2, wc+[t2[i]], s+t2[i], i+1)
    wc=[w[j] for j in range(len(w))]
    rek(t1, t2, wc+[t1[i]]+[t2[i]], s+t1[i]+t2[i], i+1)

t1=[1,3,2,4]
t2=[9,7,4,8]
rek(t1, t2, [], 0, 0)
#17:50
'''
'''
Zad. 2 Dana jest N elementowy zbiór liczb naturalnych w postaci tablicy int t[N]. Proszę napisać
funkcję, która zwraca informację czy jest możliwy podział zbioru na trzy zbiory tak aby w każdym z
trzech zbiorów lączna liczba jedynek w liczbach zapisanych w systemie binarnym była jednakowa. Na
przykład dla zbioru |Ż,3,5,7,I1",L3,J-6} możliwy podział to {2,L3,L6} {3,L1i {5,7l czyli w systemie
dwójkowym {10,1101,10000} {11,10LLI |1o1',11'L} - w każdym zbiorze jest 5 jedynek.
'''
'''
#18:40
def jedynki(n):
    licznik=0
    while(n!=0):
        if(n%2==1):
            licznik+=1
        n//=2
    return licznik

def rek(T, i, s1, s2, s3, suma):
    if(s1==s2==s3==suma//3):
        return True
    if(i==len(T)):
        return False
    return rek(T, i+1, s1+T[i], s2, s3, suma) or rek(T, i+1, s1, s2+T[i], s3, suma) or rek(T, i+1, s1, s2, s3+T[i], suma)

def f(T):
    suma=0
    for i in range(len(T)):
        T[i]=jedynki(T[i])
        suma+=T[i]
    if(suma%3!=0 and len(T)<3):
        print("nie da sie")
        exit(0)
    else:
        print(rek(T, 0, 0, 0, 0, suma))

T=[17, 0, 1]
f(T)
#19
'''
'''
Dana jest tablica int t[N] wypeªniona liczbami caªkowitymi. Prosz¦ napisa¢ funkcj¦, która sprawdza, czy
mo»liwe jest "poci¦cie" tablicy na co najmniej 2 kawaªki o jednakowych sumach elementów. Do funkcji nale»y
przekaza¢ tablic¦, funkcja powinna zwróci¢ najwi¦ksz¡ liczb¦ kawaªków, na któr¡ mo»na poci¡¢ tablic¦, lub
warto±¢ 0, je±li takie poci¦cie nie jest mo»liwe. Na przykªad: dla tablicy [1,2,3,1,5,2,2,2,6] odpowiedzi¡
powinno by¢ 4, bo [1,2,3|1,5|2,2,2|6].
'''
'''
def dzielniki(n):
    w=[]
    for i in range(2, n+1):
        if(n%i==0):
            w+=[i]
    return w[::-1]

def f(t):
    suma=0
    for i in range(len(t)):
        suma+=t[i]
    w=dzielniki(suma)
    for k in w:
        pom=suma//k
        i=0
        while(i<len(t)):
            pom-=t[i]
            i+=1
            if(pom==0):
                pom=suma//k
            if(i==len(t)):
                print("da sie", k)
                exit(0)
            elif(pom<0):
                break
    print("nmie da sie")

max=0
t= [1,2,3,1,5,2,2,2,6]
f(t)
'''
'''
1. Dwie liczby są zgodne piątkowo, jeżeli posiadają tyle samo cyfr parzystych w ich reprezentacjach w systemie
pozycyjnym o podstawie 5. Dane są dwie tablice int tab1[MAX1][MAX1], tab2[MAX2][MAX2] (MAX2 > MAX1 > 1).
Proszę napisać funkcję, która sprawdzi, czy możliwe jest takie przyłożenie tab1 do tab2, aby w pokrywającym się
obszarze co najmniej 33% odpowiadających sobie elementów z tab1 i tab2 było zgodnych piątkowo. Uwaga: należy
uwzględnić, że tab1 może tylko częściowo przykrywać tab2 (patrz rysunek), a w sprawdzanym obszarze musi znaleźć
się co najmniej jeden element
'''
'''
def piatkowy(n):
    licznik=0
    while(n!=0):
        if((n%5)%2==0):
            licznik+=1
        n//=5
    return licznik

def f(tab1, tab2):
    n1=len(tab1)
    n2=len(tab2)
    for i in range(n1):
        for j in range(n1):
            tab1[i][j]=piatkowy(tab1[i][j])
    for i in range(n2):
        for j in range(n2):
            tab2[i][j]=piatkowy(tab2[i][j])
    for i in range(n2-n1+1):
        for j in range(n2-n1+1):
            licznik=0
            for k in range(n1):
                for l in range(n1):
                    if(tab1[k][l]==tab2[i][j]):
                        licznik+=1
                    if(licznik/n1>=33/100):
                        return True
    return False
print(f(tab1, tab2))
'''
'''
2. Na zbiorze liczb całkowitych określono trzy operacje: A,B,C przekształcające liczby:
 A: zwiększa liczbę o 3;
 B: podwaja liczbę;
 C: wszystkie parzyste cyfry w liczbie zwiększa o 1, np. 2356->3357, 1999->1999.
Proszę napisać funkcję która sprawdza czy można przekształcić liczbę X na liczbę Y w nie więcej niż N krokach.
Do funkcji należy przekazać wartości X,Y,N, funkcja powinna zwrócić liczbę możliwych ciągów operacji
przekształcających liczbę X w Y (lub wartość 0 jeżeli takie przekształcenie nie istnieje). Uwaga: zabronione jest
używanie kolejno dwóch tych samych operacji.
Na przykład:
Dla X=11, Y=31, N=4 funkcja powinna zwrócić 3 bo są 3 możliwe ciągi operacji: ABA, ACBC, CABA
Dla X=11, Y=32, N=4 funkcja powinna zwrócić 0.
'''
'''
def ce(n):
    pom=n
    w=0
    i=1
    while(pom>=10):
        pom//=10
        i+=1
    while(i>0):
        if((n//(10**(i-1))%10)%2==0):
            w=10*w+n//(10**(i-1))%10+1
        else:
            w=10*w+n//(10**(i-1))%10
        i-=1
    return w


def f(X, Y, N, i, ost, op):
    if(op==ost):
        return 0
    ost=op
    if(X==Y):
        return 1
    if(i==N):
        return 0
    if(X>Y):
        return 0
    #print(X)
    return f(X+3, Y, N, i+1, ost, "A") + f(2*X, Y, N, i+1, ost, "B") + f(ce(X), Y, N, i+1, ost, "C")
print(f(11, 32, 4, 0, "", "pocz"))
'''
'''
3. Kolejne (co najmniej dwa) elementy listy o identycznej wartości pola val nazywamy podlistą stałą. Proszę napisać
funkcję, która usuwa z listy wejściowej najdłuższą podlistę stałą. Warunkiem jej usunięcia jest istnienie w liście
dokładnie jednej najdłuższej podlisty stałej. Do funkcji należy przekazać wskaźnik na pierwszy element listy.
Funkcja powinna zwrócić liczbę usuniętych elementów.
Na przykład z listy [ 1 3 3 3 5 7 11 13 13 1 2 2 2 2 3 ] należy usunąć podlistę [ 2 2 2 2 ],
a z listy [ 1 3 3 3 3 5 7 11 13 13 1 2 2 2 2 3 ] nie należy nic usuwać
'''
'''
#15:40

def f(T):
    max=0
    index=0
    pom=0
    for i in range(len(T)-1):
        p=0
        while(i+p+1<len(T)):
            if(T[i+p]==T[i+p+1]):
                p+=1
                if(p>max):
                    max=p
                    pom=1
                    index=i
                elif(p==max):
                    pom=0
            else:
                break
    if(pom==1):
        print(max+1)
        while(max+1>0):
            del T[index]
            max-=1
    if(pom==0):
        print(0)
    while(max+1>0):
        del T[index]
        max-=1
    print(T)

T=[ 1 ,3 ,3 ,3 ,3 ,5 ,7 ,11 ,13 ,13 ,1 ,2 ,2 ,2 ,2 ,3 ]
f(T)
#15:55
'''
'''
Zadanie 2.
Dana jest tablica int t[9], w której nale»y umie±ci¢ liczby od 1 do 9 tak, aby byªy speªnione warunki:
1) warto±ci na s¡siednich polach tablicy musz¡ si¦ ró»ni¢ o co najmniej 2
2) liczby pierwsze nie mog¡ zajmowa¢ s¡siednich pól tablicy
Warto±¢ 1 zostaªa ju» umieszczona w pierwszym (pod indeksem 0) elemencie tablicy. Prosz¦ napisa¢ program,
który wypisuje wszystkie poprawne rozmieszczenia liczb w tablicy.
'''
'''
#16:47
#nie wiadomo czy moga sie powtarzac zał:tak
def czy_pierwsza(n):
    if(n==0 or n==1):
        return False
    for i in range(2, int(n**(0.5))+1):
        if(n%i==0):
            return False
    return True

def f(t, i):
    if(i==9):
        print(t)
        return None
    for j in range(1, 10):
        tc=[t[p] for p in range(len(t))]
        if(abs(t[-1]-j)>=2):
            if(czy_pierwsza(t[-1])==False or czy_pierwsza(j)==False):
                f(tc+[j], i+1)
    return None
t=[1]
print(f(t, 1))
'''
'''
Zadanie 2.
Dana jest tablica t[N] zawieraj¡ca liczby naturalne. Prosz¦ napisa¢ funkcj¦, która odpowiada na pytanie,
czy z elementów tablicy (niekoniecznie wszystkich) mo»na utworzy¢ dwa równoliczne, niepuste podzbiory
o jednakowej sumie elementów. Do funkcji nale»y przekaza¢ wyª¡cznie tablic¦ t, funkcja powinna zwróci¢
warto±¢ typu bool.
'''
'''
import random

def f(T, s1, s2, i):
    if(i==len(T)):
        if(s1==s2):
            return True
        return False
    return f(T, s1+T[i], s2, i+1) or f(T, s1, s2+T[i], i+1)

T=[random.randint(1, 10) for _ in range(10)]
print(f(T, 0, 0, 0))
'''
'''
Zadanie 1.
Dana jest tablica wypeªniona liczbami naturalnymi int t[N][N] reprezentuj¡ca szachownic¦. Prosz¦ napisa¢
funkcj¦, która sprawdza, czy jest mo»liwe ustawienie dwóch wzajemnie szachuj¡cych si¦ skoczków tak, aby
suma warto±ci pól, na których stoj¡ skoczki, byªa liczb¡ pierwsz¡. Do funkcji nale»y przekaza¢ tablic¦ t,
funkcja powinna zwróci¢ warto±¢ typu bool.
'''
'''
import random

def f(T):
    max=0
    for i in range(len(T)):
        for j in range(len(T)):
            for k in ruchy:
                if(i+k[0]<len(T) and j+k[1]>=0 and j+k[1]<len(T)):
                    if(max<T[i][j]+T[i+k[0]][j+k[1]]):
                        max=T[i][j]+T[i+k[0]][j+k[1]]
    return max      

ruchy=((2,1),(2,-1),(1,2),(1,-2))
T=[[random.randint(1, 10) for _ in range(8)] for _ in range(8)]
for i in range(len(T)):
    print(T[i][:])
print(f(T))
'''
'''
1. Dane są deklaracje reprezentujące szachownicę o boku długości N:
const int N= …
int tab[N][N];
Tablica tab jest wypełniona liczbami naturalnymi. Na szachownicy umieszczamy dwa klocki domina tak, że jeden
klocek przykrywa dwa pola. Proszę napisać funkcję, która sprawdza czy istnie takie ustawianie klocków na
szachownicy, że:
- oba klocki są prostopadle do siebie,
- w żadnym wierszu ani w żadnej kolumnie nie leży więcej niż jeden klocek,
- największym wspólnym dzielnikiem 4 przykrytych liczb jest jeden.
'''
'''
#13:57
import random

def generowanie_dwuwymiarowej_tablicy():
    N=10
    T=[[random.randint(1, 10) for j in range(N)] for i in range(N)]
    for i in range(N):
        print(T[i][:])
    return T

def dzielniki(n):
    w=[]
    for i in range(1, n+1):
        if(n%i==0):
            w.append(i)
    return w

def najwiekszy_dzielnik(a, b, n, m):
    a=dzielniki(a)
    b=dzielniki(b)
    n=dzielniki(n)
    m=dzielniki(m)
    for k in a[::-1]:
        if k in b and k in n and k in m:
            if(k==1):
                return True
            return False

def f(T, i, j, row, col, p):
    if(najwiekszy_dzielnik(T[i][j], T[i][j+1], T[row][col], T[row+1][col])==True and p==1):
        print("tak", i, j, row, col)
        exit(0)
    for k in range(len(T)-1):
        for l in range(len(T)):
            if(k!=i and k+1!=i and l!=j and l!=j+1):
                f(T, i, j, k, l, 1)

T=generowanie_dwuwymiarowej_tablicy()

for i in range(len(T)):
    for j in range(len(T)-1):
        f(T, i, j, 0, 0, 0)

#14:14
'''
'''
Ład. L Dana jest tablica int t[N][N] zawierająca liczby naturalne. Dokładnie w jednym z wierszy
tablicy znajduje się fragment ciągu Fibonacciego o długościwiększej niż 2,a mniejszej niż N. Proszę
napisać funkcję, która odszuka ten fragment ciągu i zwróci numer wiersza w którym on się znajduje.
'''
'''
#13:33
def f(T, N):
    max=0
    maxi=-1
    for i in range(len(T)):
        for j in range(len(T)-2):
            p=0
            while(T[i][j+p]==T[i][j+1+p]==T[i][j+2+p]):
                if(p>max):
                    max=p
                    maxi=i
                    if(max+3==N-1):
                        return max+3, maxi
                if(j+2+p<len(T)):
                    p+=1
                
    return max+3, maxi
T=[[1,2,3],[1,1,2],[1,7,5]]
print(f(T, N))
#chyba dobrze ale ciezko stwierdzic
'''
'''
Zadanie 2.
Dana jest tablica t[N] zawieraj¡ca liczby naturalne. Prosz¦ napisa¢ funkcj¦, która odpowiada na pytanie,
czy z elementów tablicy (niekoniecznie wszystkich) mo»na utworzy¢ dwa równoliczne, niepuste podzbiory
o jednakowej sumie elementów. Do funkcji nale»y przekaza¢ wyª¡cznie tablic¦ t, funkcja powinna zwróci¢
warto±¢ typu bool.
'''
'''
#14:50 20 min
def f(T, i, s1, s2, l, p):
    if(s1==s2 and l==p and l!=0):
        return True
    if(i==len(T)):
        return False
    if(l==len(T)//2+1 or p==len(T)//2+1):
        return False
    return f(T, i+1, s1+T[i], s2, l+1, p) or f(T, i+1, s1, s2+T[i], l, p+1) or f(T, i+1, s1, s2, l, p)

T=[1, 2, 3, 6, 17, 50]
print(f(T, 0, 0, 0, 0, 0))
#14:56
'''
'''
2. Proszę napisać program, który wypełnia tablicę int tab[MAX] trzycyfrowymi liczbami
pseudolosowymi, a następnie wyznacza i wypisuje długość najdłuższego podciągu spójnego
znajdującego się w tablicy dla którego w tablicy występuje również rewers tego ciągu.
Na przykład dla tablicy: 2,9,3,1,7,11,9,6,7,7,1,3,9,12,15 odpowiedzią jest liczba 4
'''
'''
#15:00
import random

def tab(MAX):
    T=[random.randint(100, 999) for _ in range(MAX)]
    return T

def f(T):
    max=0
    for i in range(len(T)-1):
        pocz=len(T)-1
        while(pocz>i):
            p=0
            while(T[i+p]==T[pocz-p]):
                if(p>max):
                    max=p
                p+=1
                if(i+p>=pocz-p):
                    break
            pocz-=1
            
    return max+1

T=[2,9,3,1,7,11,9,6,7,7,1,3,9,12,15]
print(f(T))
#15:10; 40
#15:45
'''
'''
1. Dana jest liczba naturalna N niezawierająca cyfry 0, którą rozbijamy na dwie liczby naturalne
A i B, przenosząc kolejne cyfry z liczby N do liczby A albo B. Na przykład liczbę 21523
możemy rozbić na wiele sposobów, np. (215,23),(2,1523),(223,15),(152,23),(22,153),(1,2523)...
Uwaga: względna kolejność cyfr w liczbie N oraz liczbach A i B musi być zachowana. Proszę
napisać funkcję generującą i wypisującą wszystkie rozbicia, w których powstałe liczby A i B
są względnie pierwsze. Do funkcji należy przekazać wartość N, funkcja powinna zwrócić liczbę
znalezionych par.
Uwagi:
- warunek względnej pierwszości można pominąć kosztem 1 pkt
- do funkcji można przekazać dodatkowe parametry
- czas na rozwiązanie obu zadań wynosi 45 minut
- za każde zadanie można otrzymać maksymalnie 5 pkt
- oceniane będą: czytelność, poprawność i efektywność rozwiązań
'''
'''
#15:45

def wzgl_pierw(a, b):
    if(a>b):
        for i in range(2, b+1):
            if(a%i==0 and b%i==0):
                return False
    else:
        for i in range(2, a+1):
            if(a%i==0 and b%i==0):
                return False
    return True

def f(N, i, l, p, dl):
    if(i==dl):
        if(wzgl_pierw(l, p)==True):
            print(l, p)
            global licznik
            licznik+=1
        return
    f(N, i+1, 10*l+(N//10**(dl-i-1))%10, p, dl)
    f(N, i+1, l, 10*p+(N//10**(dl-i-1))%10, dl)

licznik=0
N=21523
NC=N
dl=1
while(NC>=10):
    dl+=1
    NC//=10
f(N, 0, 0, 0, dl)
print(licznik)
'''
'''
1) Dane są trzy operacje na liczbach naturalnych oznaczone literami ĄB,C. A. jeżeli liczba posiada co najmniej 2 cyfry zamienia miejscami dwie ostatnie cyfry w liczbie;
B. mnoży liczbę przez3;
c. jeżeli liczba posiada co najmniej 2 cyfry usuwa pierwszą cyfrę z liczby.
Proszę napisać funkcję, która szuka sekwencji operacji przekształcającej liczbę naturalną x na y (x!=y) o długości nie większej niż 7. Do funkcji
należy przekazać liczby x, y. Funkcja powinna zwrócić napis złożony z liter ABC realizujący przekształcenie albo łańcuch pustyjeżeli
przekształcenie nie istnieje. Na przykład dla liczb 6,3 funkcja powinna zwrócić napis "BACB".
Uwagi:
o do funkcji można przekazać dodatkowe parametry.
. czas na rozwiązanie zadań wynosi 40 min .
o za każde zadanie można otrzymać maksymalnie 5 pkt.
o oceniane będą: czytelność, poprawność i efektywność rozwiązań
'''
'''
#10:25

def dlugosc(n):
    dl=1
    while(n>=10):
        dl+=1
        n//=10
    return dl

def f(x, y, N, i, w):
    if(i==7):
        return
    if(x==y):
        print(w)
        exit(0)
        return
    dl=dlugosc(x)
    if(dl>=2):
        a=x%10
        b=(x//10)%10
        f(x//100+b+10*a, y, N, i+1, w+"A")
        f(x - ( ( ( x//(10**(dl-1)))%10) * ( 10**( dl - 1 ) ) ), y, N, i+1, w+"C")
    f(3*x, y, N, i+1, w+"B")

print(f(7, 12, 7, 0, ""))
#10:42
'''
'''
1. Na szachownicy o wymiarach 201 wierszy i 201 kolumn umieszczamy 100 króli szachowych. Proszę
napisać program, który wczytuje z klawiatury położenia 100 króli (wiersz, kolumna), odnajduje dwa
króle jednakowo odległe od środka szachownicy i wypisuje ich pozycję (wiersz, kolumna). W
przypadku gdy żadna para króli nie spełnia warunku program kończy się stosownym komunikatem.
Odległość króla od środka to liczba jego ruchów, które musi wykonać aby dotrzeć do środka
szachownicy.
Uwagi:
1. Król może przesunąć się na dowolne z 8 sąsiednich pól
2. Można założyć, że dane wprowadzone z klawiatury będą poprawne
3. Licząc drogę króla zakładamy, że szachownica jest pusta
'''
'''
#10:58

def f(T):
    for i in range(101):
        for j in range(101):
            if(T[i][j]==T[200-i][j]==1 or T[i][j]==T[200-i][200-j]==1 or T[i][j]==T[i][200-j]==1 or T[i][200-j]==T[200-i][j]==1 or T[200-i][200-j]==T[200-i][j]==1 or T[i][200-j]==T[200-i][200-j]==1):
                #podzielic na 6 ifow i gotowe
                return True
    return False


T=[[0 for _ in range(201)] for _ in range(201)]
for i in range(100):
    row=int(input("podaj wiersz {}. króla".format(i)))
    col=int(input("podaj kolumnę {}. króla".format(i)))
    while(T[row][col]==1):
        row=int(input("podaj wiersz {}. króla".format(i)))
        col=int(input("podaj kolumnę {}. króla".format(i)))
    T[row][col]=1
'''
'''
2. Wyrazy budowane są z liter a..z. Dwa wyrazy „ważą” tyle samo jeżeli: mają tę samą liczbę
samogłosek oraz sumy kodów ascii liter z których są zbudowane są identyczne, na przykład „ula” ->
117 108 97 oraz „exe” 101 120 101. Proszę napisać funkcję bool wyraz( string s1, string s2), która
sprawdza czy jest możliwe zbudowanie wyrazu z podzbioru liter zawartych w s2 ważącego tyle co
wyraz s1. Dodatkowo funkcja powinna wypisać znaleziony wyraz
'''
'''
1. Na szachownicy o wymiarach 201 wierszy i 201 kolumn umieszczono pewną liczbę wież
szachowych tak, że każde z pól na jest szachowane. Przyszedł zły człowiek i zmienił położenie jednej z
wież na szachownicy, tak że nie wszystkie pola są szachowane. Proszę zaproponować funkcję, która
znajdzie przeniesienie jednej wieży tak aby ponownie wszystkie pola były szachowane. Do funkcji
przekazujemy tablicę bool t[201][201] z układem wież po zmianie, funkcja powinna wyznaczyć i
zwrócić dwa pola (wiersz, kolumna) – skąd , dokąd należy przenieść wieżę.
'''
'''
#11:35

def f(T):
    w=[]
    for i in range(len(T)):
        p=0
        for j in range(len(T)):
            if(T[i][j]==1):
                p+=1
        w.append(p)
    k=[]
    for i in range(len(T)):
        p=0
        for j in range(len(T)):
            if(T[j][i]==1):
                p+=1
        k.append(p)
    print(w, k)
    a, b = (-1, -1), (-1, -1)
    for i in range(len(T)):
        for j in range(len(T)):
            if(w[i]==k[j]==0):
                a=(i, j)
    for i in range(len(T)):
        for j in range(len(T)):
            if(w[i]==k[j]>1):   
                b=(i, j)
    return a, b

T=[[0 for _ in range(201)] for _ in range(201)]
for i in range(len(T)):
    T[i][i]=1
T[2][2]=0
T[0][1]=1

print(f(T))

#11:45
'''
'''
1. Dana jest tablica wypełniona liczbami naturalnymi:
const int N=1000; int t[N][N];
Proszę napisać funkcję, która poszukuje w tablicy kwadratu o liczbie pól będącej liczbą nieparzystą
większą od 1, którego iloczyn 4 pól narożnych wynosi k. Do funkcji należy przekazać tablicę i wartość
k. Funkcja powinna zwrócić informacje czy udało się znaleźć kwadrat oraz współrzędne (wiersz,
kolumna) środka kwadratu. 
'''
'''
def f(T, k):
    dl=3
    while(dl<=len(T)):
        for i in range(len(T)-dl+1):
            for j in range(len(T)-dl+1):
                if(T[i][j]*T[i+dl-1][j+dl-1]*T[i+dl-1][j]*T[i][j+dl-1]==k):
                    return i+dl//2+1, j+dl//2+1 
        dl+=2
    return False
T=[[0 for _ in range(10)] for _ in range(10)]
T[0][0]=1
T[4][4]=1
T[0][4]=1
T[4][0]=1
print(f(T, 1))
'''
'''
1. Dana jest tablica wypełniona liczbami naturalnymi:
const int N=1000;
int t[N][N];
Proszę napisać funkcję, która w poszukuje w tablicy najdłuższego ciągu geometrycznego leżącego ukośnie w kierunku
prawo-dół, liczącego co najmniej 3 elementy. Do funkcji należy przekazać tablicę. Funkcja powinna zwrócić
informacje czy udało się znaleźć taki ciąg oraz długość tego ciągu.
'''
'''
#12:12
def f(T):
    max=0
    for i in range(len(T)-2): #wybor kolumny (cz. prawa górna)
        p=0
        while(p<len(T)-2-i):
            licznik=0
            q=T[p+1][i]/T[p][i]
            if(T[p+2][i]/T[p+1][i]==q):
                p+=1
                licznik+=1
                if(licznik>max):
                    max=licznik
            else:
                licznik=0

    for i in range(2,len(T)): #wybor kolumny (cz. lewa dolna)
        p=0
        while(p<len(T)-2-i):
            licznik=0
            q=T[i-p-1][i]/T[i-p][i]
            if(T[i-p-2][i]/T[i-p-1][i]==q):
                licznik+=1
                p+=1
                if(licznik>max):
                    max=licznik
            else:
                licznik=0
    return max+2

T=[
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 4, 4],
    [1, 2, 3, 4]
]
print(f(T))
#12:27 ciężary
'''
'''
#2011-2012 k1
#12:47
def zamiana(n, i):
    max=0
    licznik=1
    ostatnia=n%i
    n//=i
    while(n!=0):
        if(n%i<=ostatnia):
            licznik+=1
            if(licznik>max):
                max=licznik
        else:
            licznik=1
        ostatnia=n%i
        n//=i
    return max

def f(n):
    max=0
    for i in range(2, 9):
        if(zamiana(n, i)>max):
            if(4==zamiana(n, i)):
                return True
    return False
            
print(f(143))
#12:55
'''
'''
#2011-12 k2
#12:56
#T=[(x, y), (x1, y1), ...]
def f(T):
    for k in T:
        p=1
        while(k[0]+p<len(T) and k[1]+p<len(T)):
            if((k[0]+p, k[1+p]) in T):
                return True
            p+=1
        p=-1
        while(k[0]+p>=0 and k[1]+p>=0):
            if((k[0]+p, k[1+p]) in T):
                return True
            p-=1
        p=1
        while(k[0]+p<len(T)):
            if((k[0]+p, k[1]) in T):
                return True
            p+=1
        p=-1
        while(k[0]+p>=0):
            if((k[0]+p, k[1]) in T):
                return True
            p-=1
        p=1
        while(k[1]+p<len(T)):
            if((k[0], k[1+p]) in T):
                return True
            p+=1
        p=-1
        while(k[1]+p>=0):
            if((k[0], k[1+p]) in T):
                return True
            p-=1
        
    return False

print(f(T))
'''
'''
3. Dane są trzy listy jednokierunkowe uporządkowane rosnąco bez powtarzających się
liczb. Proszę napisać funkcję która usunie w każdej liście elementy powtarzające się
w trzech listach. Funkcja ma zwrócić liczbę usuniętych elementów.
'''
'''
class Node:
    def __init__(self, val=None):
        self.val=val
        self.next=None

def dodaj(zbior, element):
    if(zbior==None):
        nowy=Node(element)
        return nowy
    prev=None
    curr=zbior
    while(curr!=None):
        if(curr.val==element):
            return zbior
        prev=curr
        curr=curr.next
    nowy=Node(element)
    prev.next=nowy
    return zbior

def wypisz(zbior):
    while(zbior!=None):
        print(zbior.val,end=" ")
        zbior=zbior.next

#do 19:21
def f(zbior1, zbior2, zbior3):
    licznik=0
    if(zbior1==None or zbior2==None or zbior3==None):
        return licznik
    else:
        a,b,c=0,0,0
        while((a==0 or b==0 or c==0) and (zbior1!=None and zbior2!=None and zbior3!=None)):
            print(zbior1.val,zbior2.val,zbior3.val, "a")
            if(zbior1.val==zbior2.val==zbior3.val):
                licznik+=1
                print(zbior1.val)
                zbior1, zbior2, zbior3 = zbior1.next, zbior2.next, zbior3.next
            if(zbior1.val>zbior2.val or zbior2.val<zbior3.val):
                zbior2=zbior2.next
                b=1
            elif(zbior1.val<zbior2.val or zbior1.val<zbior3.val):
                zbior1=zbior1.next
                a=1
            if(zbior3.val<zbior1.val or zbior3.val<zbior2.val):
                zbior3=zbior3.next
                c=1
        if(zbior1==None or zbior2==None or zbior3==None):
            return licznik

        kopia1, kopia2, kopia3 = zbior1.next, zbior2.next, zbior3.next
        prev1, prev2, prev3 = zbior1, zbior2, zbior3
        while(kopia1!=None and kopia2!=None and kopia3!=None):
            print(kopia1.val,kopia2.val,kopia3.val)
            if(kopia1.val==kopia2.val==kopia3.val):
                #print(kopia1.val)
                prev1.next, prev2.next, prev3.next = kopia1.next, kopia2.next, kopia3.next
                licznik+=1
            if(kopia1.val<kopia2.val):
                if(kopia1.val<kopia3.val):
                    prev1=kopia1
                    kopia1=kopia1.next
                elif(kopia3.val<kopia1.val):
                    prev3=kopia3
                    kopia3=kopia3.next
                elif(kopia1.val==kopia3.val):
                    prev1, prev3 = kopia1, kopia3
                    kopia1, kopia3 = kopia1.next, kopia3.next
            elif(kopia1.val>kopia2.val):
                if(kopia2.val<kopia3.val):
                    prev2=kopia2
                    kopia2=kopia2.next
                elif(kopia3.val<kopia2.val):
                    prev3=kopia3
                    kopia3=kopia3.next
                elif(kopia2.val==kopia3.val):
                    prev2, prev3 = kopia2, kopia3
                    kopia2, kopia3 = kopia2.next, kopia3.next
            elif(kopia1.val==kopia2.val):
                if(kopia1.val<kopia3.val):
                    prev1, prev2 = kopia1, kopia2
                    kopia1, kopia2 = kopia1.next, kopia2.next
                else:
                    prev3=kopia3
                    kopia3=kopia3.next
            
        return licznik


zbior1, zbior2, zbior3 = None, None, None
for i in range(10):
    zbior1=dodaj(zbior1, i**2)
for i in range(50):
    zbior2=dodaj(zbior2, 2*i)
for i in range(100):
    zbior3=dodaj(zbior3, i)
print(f(zbior1, zbior2, zbior3))
#nie do konca dziala
'''
'''
Zadanie 3.
Dwie listy zawieraj¡ niepowtarzaj¡ce si¦ (w obr¦bie listy) liczby naturalne. W obu listach liczby s¡ posortowane rosn¡co. Prosz¦ napisa¢ funkcj¦ usuwaj¡c¡ z ka»dej listy liczby wyst¦puj¡ce w drugiej. Do funkcji
nale»y przekaza¢ wskazania na obie listy, funkcja powinna zwróci¢ ª¡czn¡ list¦ usuni¦tych elementów.
'''
'''
class Node:
    def __init__(self, val=None):
        self.val=val
        self.next=None

def dodaj(zbior, element):
    if(zbior==None):
        nowy=Node(element)
        return nowy
    prev=None
    curr=zbior
    while(curr!=None):
        if(curr.val==element):
            return zbior
        prev=curr
        curr=curr.next
    nowy=Node(element)
    prev.next=nowy
    return zbior

def wypisz(zbior):
    while(zbior!=None):
        print(zbior.val,end=" ")
        zbior=zbior.next
#20:02
def f(lista1, lista2):
    nowa=None
    prev_nowa=None
    if(lista1==None or lista2==None):
        return nowa
    a,b=0,0
    while((a==0 or b==0) and lista1!=None and lista2!=None):
        if(lista1.val==lista2.val):
            nowa=Node(lista1.val)
            if(prev_nowa==None):
                first=nowa
                prev_nowa=nowa
            else:
                prev_nowa.next=nowa
            lista1=lista1.next
            lista2=lista2.next
        elif(lista1.val<lista2.val):
            lista1=lista1.next
            a=1
        else:
            lista2=lista2.next
            b=1
        
    prev1, prev2 = lista1, lista2
    curr1, curr2 = lista1.next, lista2.next
    while(curr1!=None and curr2!=None):
        print(curr1.val, curr2.val)
        if(curr1.val==curr2.val):
            nowa=Node(curr1.val)
            if(prev_nowa==None):
                first=nowa
                prev_nowa=nowa
            else:
                prev_nowa.next=nowa
            curr1=curr1.next
            curr2=curr2.next
        elif(curr1.val<curr2.val):
            prev1=curr1
            curr1=curr1.next
        elif(curr1.val>curr2.val):
            prev2=curr2
            curr2=curr2.next
    return first
    
lista1, lista2 = None, None
for i in range(10):
    lista1=dodaj(lista1, 2*i)
    lista1=dodaj(lista1, 3*i)
    lista1=dodaj(lista1, 5*i)
    lista2=dodaj(lista2, i**2)
nowa=f(lista1, lista2)
wypisz(nowa)
'''
'''
class Node:
    def __init__(self, val=None, next=None):
        self.val=val
        self.next=next

def dodaj(zbior, element):
    if(zbior==None):
        nowy=Node(element)
        return nowy
    prev=None
    curr=zbior
    while(curr!=None):
        if(curr.val==element):
            return zbior
        prev=curr
        curr=curr.next
    nowy=Node(element)
    prev.next=nowy
    return zbior

def wypisz(zbior):
    while(zbior!=None):
        print(zbior.val,end=" ")
        zbior=zbior.next
#11:04
def osemkowy(n):
    licznik=0
    while(n!=0):
        if(n%8==5):
            licznik+=1
        n//=8
    if(licznik%2==1):
        return True
    return False

def f(zbior):
    if(zbior==None or zbior.next==None):
        return zbior
    first=None
    prev_pocz=zbior
    prev=zbior
    zbior=zbior.next
    while(zbior!=None):
        if(osemkowy(zbior.val)==True):
            first=Node(zbior.val, prev_pocz)
            prev_pocz=first
            prev.next=zbior.next
            del zbior
            zbior=prev
        prev=zbior
        zbior=zbior.next
    return first
zbior=None
for i in range(100):
    zbior=dodaj(zbior, i)
wypisz(f(zbior))

class Node:
    def __init__(self, val=None, next=None):
        self.val=val
        self.next=next

def dodaj(zbior, element):
    if(zbior==None):
        nowy=Node(element)
        return nowy
    prev=None
    curr=zbior
    while(curr!=None):
        if(curr.val==element):
            return zbior
        prev=curr
        curr=curr.next
    nowy=Node(element)
    prev.next=nowy
    return zbior

def wypisz(zbior):
    while(zbior!=None):
        print(zbior.val,end=" ")
        zbior=zbior.next

def f(zbior1, zbior2): #zbior1 - rosnacy
    while(zbior2!=None):
        if(zbior2.val<zbior1.val):
            pom=zbior1
            zbior1 = Node(zbior2.val, pom)
        elif(zbior2.val==zbior1.val):
            zbior1=zbior1.next
        else:
            prev=zbior1
            kopia1=zbior1.next
            while(kopia1!=None):
                if(kopia1.val==zbior2.val):
                    prev.next=kopia1.next
                    break
                elif(kopia1.val>zbior2.val):
                    prev.next = Node(zbior2.val, kopia1)
                    break
                prev=kopia1
                kopia1=kopia1.next
        zbior2=zbior2.next
    return zbior1

zbior1=None
zbior2=None
zbior1=dodaj(zbior1, 2)
zbior1=dodaj(zbior1, 4)
zbior1=dodaj(zbior1, 8)
zbior1=dodaj(zbior1, 16)
zbior2=dodaj(zbior2, 17)
zbior2=dodaj(zbior2, 3)
zbior2=dodaj(zbior2, 6)
zbior2=dodaj(zbior2, 15)
zbior2=dodaj(zbior2, 8)
zbior2=dodaj(zbior2, 12)
zbior2=dodaj(zbior2, 1)
zbior2=dodaj(zbior2, 16)
zbior2=dodaj(zbior2, 17)
wypisz(f(zbior1, zbior2))
'''
'''6.031 Mamy daną liczbę całkowitą. W tablicy jednowymiarowej należy znaleźć n liczb, których suma jest równa danej liczbie.
Proszę napisać funkcję Nka, która otrzymując jako parametry (1) tablicę int t[N],) n (ilość liczb stanowiących sumę) oraz sumę sprawdza, ile można w niej znaleźć „enek”.'''
'''
#modyfikacja: printuj te sumy

def rek(T, n, suma, i, licznik, tab):
    if(suma==0 and licznik==n):
        print(tab)
        return 1
    elif(suma<0 or licznik>n):
        return 0
    if i==len(T):
        return 0
    return rek(T, n, suma, i+1, licznik, tab)+rek(T, n, suma-T[i], i+1, licznik+1, tab+[T[i]])

def f(t, n, suma):
    return rek(t, n, suma, 0, 0, [])

t=[1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
print(f(t, 3, 105))
'''
'''
class Node:
    def __init__(self, val=None, next=None):
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

def idz_do_ostatniego(zbior):
    licznik=0
    if zbior is None:
        return 0
    while zbior.next is not None:
        licznik+=1
        zbior=zbior.next
    return licznik

def wypisz(zbior):
    if zbior is None:
        print("pusty")
        return
    while zbior is not None:
        print(zbior.val, end=" ")
        zbior=zbior.next
    print()
    return

def f(zbior1, zbior2):
    licznik=0
    list1=zbior1
    list2=zbior2
    if list1 is None or list2 is None:
        return idz_do_ostatniego(list1)+idz_do_ostatniego(list2)
        #TODO: usun niepusta liste
    prev1=None
    prev2=None
    while list1 is not None and list2 is not None:
        if(list1.val==list2.val):
            prev1=list1
            list1=list1.next
            prev2=list2
            list2=list2.next
        elif(list1.val<list2.val):
            if prev1 is None:
                kopia=zbior1
                zbior1=zbior1.next
                del kopia
            else:
                licznik+=1
                kopia=list1
                prev1.next=list1.next
                del kopia
            list1=prev1.next
        else:
            if prev2 is None:
                kopia=zbior2
                zbior2=zbior2.next
                del kopia
            else:
                licznik+=1
                kopia=list2
                prev2.next=list2.next
                del kopia
                list2=prev2.next
    if list1 is None:
        prev2.next=None
        while list2 is not None:
            licznik+=1
            kopia=list2
            list2=list2.next
            del kopia
    if list2 is None:
        prev1.next=None
        while list1 is not None:
            licznik+=1
            kopia=list1
            list1=list1.next
            del kopia        
    return licznik


zbior1=utworz_linkliste_z_listy([])
zbior2=utworz_linkliste_z_listy([1,2,4,5,7,8,9])
print(f(zbior1, zbior2))
wypisz(zbior1)
wypisz(zbior2)
'''
'''
Zadanie 19. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
zwraca liczbę par elementów, o określonym iloczynie, takich że elementy są odległe o jeden ruch skoczka
szachowego.
'''
'''
def czy_mozna(T, row, col, ruch):
    if(row+ruch[0]>len(T)-1 or col+ruch[1]<0 or col+ruch[1]>len(T)-1): #nie ma ruchow w dol
        return False
    return True

def f(T, iloczyn):
    licznik=0
    ruchy=((1,2),(1,-2),(2,1),(2,-1)) #nie wykonuje ruchow w dol aby nie powtarzac sprawdzen
    for row in range(len(T)):
        for col in range(len(T)):
            for ruch in ruchy:
                if(czy_mozna(T, row, col, ruch)==True):
                    if(T[row][col]*T[row+ruch[0]][col+ruch[1]]==iloczyn):
                        licznik+=1
    return licznik
'''
'''
Zadanie 18. Dana jest tablica T[N][N] wypełniona liczbami całkowitymi. Proszę napisać funkcję, która
wyszuka spójny podciąg elementów leżący poziomo lub pionowo o największej sumie. Maksymalna długość
podciągu może wynosić 10 elementów. Do funkcji należy przekazać tablicę T, funkcja powinna zwrócić sumę
maksymalnego podciągu
'''
'''
import random

def f(T):
    max=0
    for row in range(len(T)):
        suma=T[row][0]
        last=0
        dl=1
        for col in range(1,len(T)):
            print(row, col, dl)
            if(dl==3):
                suma=suma-T[row][last]+T[row][col]
                last+=1
                if(suma>max):
                    max=suma
            elif(dl==1):
                if(0<T[row][last]):
                    suma=suma+T[row][col]
                    dl+=1
                    if(suma>max):
                        max=suma
                else:
                    suma=suma+T[row][col]-T[row][last]
                    last+=1
                    if(suma>max):
                        max=suma
            else:
                if(T[row][last]>0):
                    suma=suma+T[row][col]
                    dl+=1
                    if(suma>max):
                        max=suma
                else:
                    suma=suma-T[row][last]+T[row][col]
                    last+=1
                    if(suma>max):
                        max=suma
            print(max, suma)
        while(dl!=0):
            suma-=T[row][last]
            last+=1
            dl-=1
            if(suma>max):
                max=suma
    
    #analogicznie dla kolumn

    return max


T=[[random.randint(-100, 100) for _ in range(5)] for _ in range(5)]
for i in range(len(T)):
    print(T[:][i])
print(f(T)) 
'''
'''
Zadanie 16. Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję która
odpowiada na pytanie, czy w tablicy każdy wiersz zawiera co najmniej jedną liczbą złożoną wyłącznie z cyfr
będących liczbami pierwszymi?
'''
'''
def czy_pierwsza(n):
    if(n==0 or n==1):
        return False
    for i in range(2, int(n**(0.5))+1):
        if(n%i==0):
            return False
    return True

def f(T):
    for row in range(len(T)):
        flag=False
        for col in range(len(T)):
            w=T[row][col]
            while(w!=0):
                if(czy_pierwsza(w%10)==False):
                    break
                w//=10
                if(w==0):
                    flag=True
            if(flag==True):
                break
        if flag is False:
            return False
    return True

T=[[33, 1, 1, 1, 1],
[1, 333, 1, 1, 1],
[1, 1, 1, 7, 1],
[1, 1, 1, 333, 1],
[1, 1, 1, 1, 222]]
print(f(T))
'''
'''

Zadanie 19. Dana jest N-elementowa tablica t wypełniona liczbami naturalnymi. Proszę napisać funkcję,
która zwraca długość najdłuższego, spójnego podciągu rosnącego dla którego suma jego elementów jest
równa sumie indeksów tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość
znalezionego podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.
'''
'''
def f(T): #5 3 1 2 3 4
    prev=T[0]
    curr=T[1]
    i=1
    while(curr<=prev and i+1<len(T)):
        i+=1
        cp=curr
        curr=T[i]
        prev=cp
    if(i+1==len(T)):
        return 0
    max=2
    licznik=1
    for k in range(i, len(T)):
        curr=T[k]
        if(curr>prev):
            licznik+=1
        else:
            if(licznik>max):
                max=licznik
            licznik=1
        prev=curr
    if(licznik>max):
        return licznik
    return max
'''
'''
Zadanie 18. Dana jest N-elementowa tablica t jest wypełniona liczbami naturalnymi. Proszę napisać
funkcję, która zwraca długość najdłuższego spójnego podciągu będącego palindromem złożonym wyłącznie
z liczb nieparzystych. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość znalezionego
podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.
'''
'''
def f(T):
    max=0
    licznik=0
    for i in range(len(T)-1):
        if(T[i]%2==1):
            p=len(T)-1
            while(p>i):
                k=0
                if(T[i]==T[p]):
                    licznik+=1
                    k-=1
                    while(p>i+licznik):
                        if(T[p+k]==T[i+licznik] and T[i+licznik]%2==1):
                            licznik+=1
                            k-=1
                            if(licznik>max):
                                max=licznik
                                licznik=0
                        else:
                            if(licznik>max):
                                max=licznik
                                licznik=0
                            break
                p-=1
    return max

print(f([1,2,3,4,5,7,9,6,6,6,6,6,9,8,7,5,1,4,3]))
'''
'''
Zadanie 16. Mamy zdefiniowaną n-elementową tablicę liczb całkowitych.
Proszę napisać funkcję zwracającą wartość typu bool oznaczającą, czy w tablicy istnieje dokładnie jeden element najmniejszy i dokładnie
jeden element największy (liczba elementów najmniejszych oznacza liczbę takich elementów o tej samej
wartości)
'''
'''
def f(T):
    if(len(T)==0):
        return False
    flagl=True
    flagp=True
    max=T[0]
    min=T[0]
    for i in range(1,len(T)):
        if(T[i]==min):
            flagl=False
        elif(T[i]<min):
            flagl=True
            min=T[i]
        elif(T[i]==max):
            flagp=False
        elif(T[i]>max):
            max=T[i]
            flagp=True
    if(flagl==flagp==True):
        return True
    return False

T=[2,1,2,-1,3]
print(f(T))
'''
'''
def rozklad(n):          
    wynik=[]
    i=2
    while(n!=1):
        if(n%i==0):
            n//=i
            if(n%i==0):
                return []
            wynik.append(i)
        i+=1
    return wynik

def f(T):
    max=0
    start=0
    for i in range(len(T)):
        if(T[i]==1):
            if(i-start+1>max):
                max=i-start+1
        elif(len(rozklad(T[i]))==0):
            start=i+1
        else:
            if(i!=start):
                for dzielnik in rozklad(T[i]):
                    for index in range(start, i):
                        if(T[index]%dzielnik==0):
                            start=index+1
                if(i-start+1>max):
                    max=i-start+1
            else:
                if(1>max):
                    max=1
    return max
            
            

#t=[]
t=[2,4]
#t=[2, 7, 9, 10, 13, 5]
#t=[2,23,33,35,7,4,6,7,5,11,13,22]
print(f(t))
'''
'''
# 1, 3, 35, 4653, 345, 345, 35, 3, 1, 24, 15, 222
# 1, 3, 7, 3, 1, 3, 2
def is_palindrome(T, start, curr):
    while(start<curr):
        if(T[start]!=T[curr]):
            return False
        start+=1
        curr-=1
    return True

def f(T):
    max=0
    start=0
    for curr in range(0, len(T)):
        if(T[curr]%2==1):
            kopia=start
            while(kopia<=curr):
                if(is_palindrome(T, kopia, curr)):
                    if(curr-kopia+1>max):
                        max=curr-kopia+1
                kopia+=1
        else:
            start=curr+1
    return max
            
print(f([1, 1, 3, 1, 2, 3, 1, 5, 1, 5, 7, 8]))
'''
'''
1. Dwie liczby są zgodne piątkowo, jeżeli posiadają tyle samo cyfr parzystych w ich reprezentacjach w systemie
pozycyjnym o podstawie 5. Dane są dwie tablice int tab1[MAX1][MAX1], tab2[MAX2][MAX2] (MAX2 > MAX1 > 1).
Proszę napisać funkcję, która sprawdzi, czy możliwe jest takie przyłożenie tab1 do tab2, aby w pokrywającym się
obszarze co najmniej 33% odpowiadających sobie elementów z tab1 i tab2 było zgodnych piątkowo. Uwaga: należy
uwzględnić, że tab1 może tylko częściowo przykrywać tab2 (patrz rysunek), a w sprawdzanym obszarze musi znaleźć
się co najmniej jeden element.
'''
'''
def piatkowy(n):
    licznik=0
    i=2
    while(n!=0):
        if(n%2==0):
            licznik+=1
        n//=5
        i+=1
    return licznik

def f(tab1, tab2):
    for i in range(-len(tab1)+1,len(tab2)+len(tab1)-1):
        for j in range(-len(tab1)+1,len(tab2)+len(tab1)-1):
            licznik=0
            for row in range(len(tab1)):
                for col in range(len(tab1)):
                    if(row>=0 and row<len(tab2) and col>=0 and col<len(tab2)):
                        if(piatkowy(tab1[row][col])==piatkowy(tab2[row][col])): #zakladam ze nie mozna zmieniac wartosci tablic
                            licznik+=1
            if(licznik/(len(tab1)**2)>0.33):
                print(licznik, tab1[row][col])
                return True
    return False
            

tab2=[
    [1,2,3,67],
    [4,5,6,87],
    [7,8,9,67],
    [54,5,23,123]
]
tab1=[
    [8,4356,15],
    [17,5,6],
    [39,8,9]
]
print(f(tab1,tab2))
'''
'''
# 5 2 4
# 2 7
#-roz=-(3-2)=-1
# 5 2 4
#   2 7

class Node:
    def __init__(self, val=None, next=None):
        self.val=val
        self.next=next

def wypisz_bez_ost(zbior):
    if zbior is None: #nie ma znaczenia
        print("pusty")
        return
    while zbior.next is not None: 
        print(zbior.val, end=" ")
        zbior=zbior.next
    
    print()
    return

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

def rek(liczba1, liczba2, p, wynik):
    if liczba1==None: #warunek konca; liczba1 i liczba2 skoncza sie naraz przez poczatkowy indeks <=0
        return 0
    nowy=Node(0)
    if(p<0):
        suma=liczba1.val+rek(liczba1.next, liczba2, p+1, nowy) #cyfra liczby 1 + tail
        if(suma>=10):
            wynik.val=suma%10
            wynik.next=nowy
            tail=1
        else:
            wynik.val=suma
            wynik.next=nowy
            tail=0
        return tail
    else:
        suma=liczba1.val+liczba2.val+rek(liczba1.next, liczba2.next, p+1, nowy) #odpowiednia cyfra liczby 1 + odpowiednia cyfra liczby 2 + tail
        if(suma>=10):
            tail=1
            wynik.val=suma%10
            wynik.next=nowy
        else:
            tail=0
            wynik.val=suma
            wynik.next=nowy
        return  tail

def f(liczba1, liczba2):
    dl1, dl2 = 0, 0 #sprawdzam dlugosci obu liczb
    kopia=liczba1
    while kopia is not None:
        kopia=kopia.next
        dl1+=1
    kopia=liczba2
    while kopia is not None:
        kopia=kopia.next
        dl2+=1
    if(dl1>dl2): #wybieram tak aby liczba o wiekszej dlugosci byla liczba 1
        roznica=dl2-dl1 #poczatkowy indeks od ktorego bede decydowal czy wykonywac operacje dodawania na obu liczbach czy tylko jednej
    else:
        roznica=dl1-dl2
        liczba1, liczba2 = liczba2, liczba1
    nowy=Node(None)
    #wynik tak na prawde ma 0 na koncu; mozna je usunac ale nie wiem czy jest to potrzebne; wypisuje po prostu bez ostatniej cyfry; mozna latwo zmienic jesli trzeba
    if(rek(liczba1, liczba2, roznica, nowy)==1): #odpowienio rozdzielam pierwsza cyfre aby nie byla wieksza niz 10
        pierwszy=Node(1, nowy)
        wynik=pierwszy
    else:
        wynik=Node(0)
        wynik.next=nowy
        wynik=wynik.next
    wypisz_bez_ost(wynik)
    return #nic nie zwracam, ale rownie dobrze moge zwrocic wynik i wyprintowac wynik poza funkcja

f(utworz_linkliste_z_listy([1, 1, 1, 1]), utworz_linkliste_z_listy([9, 9, 9]))
'''
'''
2. W grze mag-mino wykorzystuje się klocki, które mają kształt prostokątów, na których obydwu końcach znajduje
się liczba oczek od 0 do 9. Na każdym klocku z dwóch jego końców liczba oczek jest inna. W komplecie liczącym 90
klocków do gry występują wszystkie kombinacje oczek i każda kombinacja występuje dokładnie jeden raz. Proszę
napisać funkcję, która dla danego zbioru N klocków wyznacza najdłuższy ciąg jaki można z nich ułożyć.
Na przykład dla zbioru 8 klocków: [2|8] [0|1] [2|3] [3|6] [2|6] [2|9] [3|4] [6|7]
najdłuższy ciąg jaki można ułożyć ma długość 5 i ma postać : [8|2] [2|3] [3|6] [6|2] [2|9]
'''
'''
def rek(T, ostatni, licznik):
    global max
    if(0==len(T)):
        if(max<licznik):
            max=licznik
        return
    for klocek in T:
        if(klocek[0]==ostatni):
            T.remove(klocek)
            rek(T, klocek[1], licznik+1)
        elif(klocek[1]==ostatni):
            T.remove(klocek)
            rek(T, klocek[0], licznik+1)
        else:
            if(max<licznik):
                max=licznik
    return
        
def f(T):
    for element in T:
        T.remove(element)
        rek(T, element[0], 1)
        rek(T, element[1], 1)
        T.append(element)
    global max
    return max

max=0
T=[[2,8], [0,1], [2,3], [3,6], [2,6], [2,9], [3,4], [6,7]]
print(f(T))
'''
'''
Zad. 1. Dane są dwie tablice int t1[N], int t2[N] wypełnione liczbami naturalnymi. Proszę napisać funkcję, która
sprawdza czy z każdej z tablic można wyciąć po jednym kawałku, tak aby suma elementów w obu kawałkach była:
co najmniej drugą potęgą dowolnej liczby naturalnej. Łączna długości obu kawałków powinna wynosić 24.
'''
'''
def potega(suma):
    if(suma==1 or suma==0):
        return True
    i=2
    while(i<suma**(0.5)+1):
        k=2
        while(i**k<=suma):
            if(i**k==suma):
                return True
            k+=1
        i+=1
    return False

def rek(t1, t2, i, l, p, suma_1, suma_2):
    if(l+p==24):
        if(potega(suma_1+suma_2)==True):
            print(suma_1+suma_2)
            return True
        return False
    if(i==len(t1)):
        return False
    return rek(t1, t2, i+1, l+1, p, suma_1+t1[i], suma_2) or rek(t1, t2, i+1, l, p+1, suma_1, suma_2+t2[i]) or rek(t1, t2, i+1, l+1, p+1, suma_1+t1[i], suma_2+t2[i])     

def f(t1, t2): #nie zakladam ze kawalek jest spojny
    return rek(t1, t2, 0, 0, 0, 0, 0)

t1=[1,2,3,4,5,6,7]
t2=[5,6,7,8,3,100,100]
print(f(t1, t2))
'''
'''
3. Kolejne (co najmniej dwa) elementy listy o identycznej wartości pola val nazywamy podlistą stałą. Proszę napisać
funkcję, która usuwa z listy wejściowej najdłuższą podlistę stałą. Warunkiem jej usunięcia jest istnienie w liście
dokładnie jednej najdłuższej podlisty stałej. Do funkcji należy przekazać wskaźnik na pierwszy element listy.
Funkcja powinna zwrócić liczbę usuniętych elementów.
Na przykład z listy [ 1 3 3 3 5 7 11 13 13 1 2 2 2 2 3 ] należy usunąć podlistę [ 2 2 2 2 ],
a z listy [ 1 3 3 3 3 5 7 11 13 13 1 2 2 2 2 3 ] nie należy nic usuwać
'''
'''
class Node:
    def __init__(self, val=None, next=None):
        self.val=val
        self.next=next

def wypisz(zbior):
    if zbior is None:
        print("pusty")
        return
    while zbior is not None:
        print(zbior.val, end=" ")
        zbior=zbior.next
    print()
    return

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

def f(zbior):
    if zbior is None or zbior.next is None:
        return 0
    prev=zbior
    curr=zbior.next
    max=0
    flag=False
    licznik=0
    max_prev=None
    while curr is not None:
        if(curr.val==prev.val):
            if(licznik==0):
                pom=prev
            licznik+=1
            if(licznik+1==max):
                flag=False
            elif(licznik+1>max):
                max=licznik+1
                max_prev=pom
                flag=True
        else:
            licznik=0
        prev=curr
        curr=curr.next
    if(flag==False):
        return 0
    else:
        if max_prev is zbior:
            while(zbior is not None and zbior.val==max_prev.val):
                kopia=zbior
                zbior=zbior.next
                del kopia
        else:
            prev=zbior
            curr=zbior.next
            while(curr!=max_prev):
                prev=curr
                curr=curr.next
            kopia=prev
            while(curr is not None and curr.val==max_prev.val):
                kopia.next=curr.next
                prev=curr
                curr=curr.next
                del prev
        return max

zbior=utworz_linkliste_z_listy([ 1,1,1,1,1,1,1,1, 3, 3, 3, 5, 7, 11, 13, 13, 1, 2, 2, 2, 2, 3 ])
print(f(zbior))
'''
'''
def dlugosc(n): #dlugosc liczby (ilosc cyfr)
    dl=1
    while(n>=10):
        dl+=1
        n//=10
    return dl

def czy_pierwsza(n): #spr czy liczba jest pierwsza
    if(n==0 or n==1):
        return False
    for i in range(2, int(n**(0.5))+1):
        if(n%i==0):
            return False
    return True

def ostatnia_cyfra(n, dl, i):
    return (n//(10**(dl-i-1)))%10    

def rek(n, w, podzialy, i, dl):
    if(i==dl):
        if(czy_pierwsza(w)):
            if(czy_pierwsza(podzialy)):
                return True
            return False
        return False
    if(czy_pierwsza(w)):
        return rek(n, 10*w+ostatnia_cyfra(n, dl, i), podzialy, i+1, dl) or rek(n, ostatnia_cyfra(n, dl, i), podzialy+1, i+1, dl)
    return rek(n, 10*w+ostatnia_cyfra(n, dl, i), podzialy, i+1, dl)

def divide(N):
    dl=dlugosc(N)
    return rek(N, 0, 1, 0, dl)

print(divide(21722))
print(divide(2222))
print(divide(273))
'''
'''
Zad. 3. Dana jest tablica t[N][N] wypełniona liczbami całkowitymi. Tablica reprezentuje szachownicę. Proszę napisać
funkcję, która sprawdza czy da się umieścić w każdym wierszu jednego króla szachowego tak aby żadne dwa króle
nie stały w odległości mniejszej niż dwa ruchy króla. Dodatkowo, suma wartości pól zajmowanych przez wszystkie
figury była równa zero.
'''
'''
def sprawdzenie(row, col, rozmieszczenia): #format rozmieszczenia: [kolumna, kolumna, ... ]
    #wystarczy sprawdzac 2 ostatnie rzedy
    if(len(rozmieszczenia)==0):
        return True
    elif(len(rozmieszczenia)==1):
        if(abs(col-rozmieszczenie[0])<=2):
            return False
        return True
    if(abs(col-rozmieszczenie[len(rozmieszczenie)-1] or abs(col-rozmieszczenie[len(rozmieszczenie)-2])<=2):
        return False
    return True
        
    

def rek(T, suma, row, rozmieszczenie):
    if(row==len(T)): #koniec
        if(suma==0): #warunek konca True
            global flag
            flag=True
            return
        return
    for col in range(len(T)):
        if(sprawdzenie(row, col, rozmieszczenie)==True):
            rek(T, suma+T[row][col], row+1, rozmieszczenie+[col])
    return
        
    

def f(T):
    rek(T, 0, 0, [])
    global flag
    return flag

flag=False

#zle zrozum.
'''
'''
#12:40
def skroc(krotka):
    if(krotka[0]==0):
        return (0,1)
    a=krotka[0]
    b=krotka[1]
    for i in range(2,krotka[0]+1):
        while(a%i==0 and b%i==0):
            a//=i
            b//=i
    if(a<0 and b<0):
        b*=-1
        a*=-1
    elif(b<0):
        b*=-1
        a*=-1
    return (a,b)

def longest(T):
    max=1
    licznik=1
    for i in range(1,len(T)):
        if(licznik==1):
            if(T[i-1][0]==0):
                q=(0,1)
            else:
                q=skroc((T[i][0]//T[i-1][1], T[i][1]//T[i-1][1]))
            licznik+=1
            print(q)
        else:
            a=T[i-1][0]*q[0]
            b=T[i-1][1]*q[1]
            prev=skroc((a,b))
            if(T[i][0]==0): #dodac
                pass
            ulamek=skroc((T[i][0],T[i][1]))
            if(prev[0]==ulamek[0] and prev[1]==ulamek[1]):
                licznik+=1
                if(licznik>max):
                    max=licznik
            else:
                licznik=1
    if(max<=2):
        return 0
    else:
        return max

#print(longest( [(0,2),(1,2),(2,2),(4,2),(4,1),(5,1)] ) # wypisze 4
#print(longest( [(1,2),(-1,2),(1,2),(1,2),(1,3),(1,2)] ) # wypisze 3
#print(longest( [(3,18),(-1,6),(7,42),(-1,6),(5,30),(-1,6)] ) # wypisze 6
#print(longest( [(1,2),(2,3),(3,4),(4,5),(5,6)] ) # wypisze 0
print(longest([(1,2),(1,7),(2,14),(4,28),(1,7),(2,2)]))
'''
'''
def rek(slowo, samogloski, flaga, i): #flaga 0-nie mozna, 1-mozna (podzielic)
    if(i==len(slowo)):
        if(flaga==1):
            return 1
        else:
            return 0
    if slowo[i] in samogloski:
        if(flaga==0):
            return rek(slowo, samogloski, 1, i+1) + rek(slowo, samogloski, 0, i+1)
        else:
            return 0
    else:
        if(flaga==0):
            return rek(slowo, samogloski, 0, i+1)
        else:
            return rek(slowo, samogloski, 0, i+1) + rek(slowo, samogloski, 1, i+1)

def cutting(s):
    samogloski=["a","e","i","o","u","y"]
    if s[0] in samogloski:
        return rek(s, samogloski, 1, 1) + rek(s, samogloski, 0, 1)
    else:
        return rek(s, samogloski, 0, 1)
    
print(cutting("student")) # wypisze 2 bo stu-dent, stud-ent
print(cutting("sesja")) # wypisze 3 bo se-sja, ses-ja, sesj-a
print(cutting("ocena")) # wypisze 4 bo o-ce-na, o-cen-a, oc-e-na, oc-en-a,
print(cutting("informatyka")) # wypisze 36
'''
'''
class Node:
    def __init__(self, val=None, next=None):
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

def check(head, r):
    curr=head.next
    prev=head
    if(r>=0):
        while curr is not None:
            a=prev.val
            b=curr.val
            while(a<b):
                a+=r
            if(a==b):
                prev=curr
                curr=curr.next
            else:
                return False
        return True
    else:
        while curr is not None:
            a=prev.val
            b=curr.val
            while(a>b):
                a+=r
            if(a==b):
                prev=curr
                curr=curr.next
            else:
                return False
        return True

def repair(head):
    curr=head.next
    prev=head
    min=curr.val-prev.val
    flag=0
    if(min<0):
        flag=1
    while curr is not None:
        if(curr.val-prev.val<min):
            min=curr.val-prev.val
        prev=curr
        curr=curr.next
    if(min==0):
        return head
    if(flag==0):
        while(min>0):
            if(check(head, min)==True):
                curr=head.next
                prev=head
                while curr is not None:
                    while(prev.val+min!=curr.val):
                        prev.next=Node(prev.val+min, curr)
                        prev=prev.next
                    prev=curr
                    curr=curr.next
                return head        
            min-=1
    else:
        while(min<0):
            if(check(head, min)==True):
                curr=head.next
                prev=head
                while curr is not None:
                    while(prev.val+min!=curr.val):
                        prev.next=Node(prev.val+min, curr)
                        prev=prev.next
                    prev=curr
                    curr=curr.next
                return head        
            min+=1
'''
'''
#18:25

def rozklad(n): #rozklad liczby na czynniki pierwsze
    W=[]
    i=2
    while(n!=1 and i<=n):
        if(n%i==0):
            W.append(i)
            n//=i
            while(n%i==0):
                n//=i
        i+=1
    return W

def czy_jeden(A,B):
    licznik=0
    for el in A:
        if el in B:
            licznik+=1
            if(licznik>1):
                return False
    return True

def four(T):
    for i in range(len(T)):
        for j in range(len(T)):
            T[i][j]=rozklad(T[i][j])
    licznik=0
    for row in range(1, len(T)-1):
        for col in range(1, len(T)-1):
            if(czy_jeden(T[row][col], T[row-1][col])==True and czy_jeden(T[row][col], T[row+1][col])==True and czy_jeden(T[row][col], T[row][col-1])==True and czy_jeden(T[row][col], T[row][col+1])==True):
                licznik+=1
    return licznik

T=[
    [1,24,15],
    [49,15,15],
    [43,14,19]
]
print(four(T))
'''