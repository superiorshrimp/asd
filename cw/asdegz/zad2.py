#Szymon Żychowicz
'''
wirtualnie rozdzielam wierzchołki zależnie od kierunku i szybkości
wykonuję algorytm dijkstry na macierzach O(12*V^2)=O(V^2)
można było tez wykonać to BFSem ale złożoność była by podobna O(60/5*(E+V^2))=O(E+V^2), a implementacja przynajmniej dla mnie trudniejsza (60/5 bo do kolejki wstawiam odleglosci podzielone na 5)
'''

from zad2testy import runtests
from math import inf

def ruchy(n):
    ruchy=((1, 0), (0, -1), (-1, 0), (0, 1))
    return ruchy[n]

def robot( L, A, B ):
    Dist=[ [ [ [ inf for vel in range(3) ] for kier in range(4) ] for x in range(len(L[0])) ] for y in range(len(L))]
    Dist[A[1]][A[0]][0][0]=0
    Proc=[ [ [ [ False for vel in range(3) ] for kier in range(4) ] for x in range(len(L[0])) ] for y in range(len(L))]
    procd=0
    while procd<=len(L)*len(L[0])*12:
        #szukanie najmniejszej odległości:
        min_id=None
        minimum=inf
        for y in range(len(L)):
            for x in range(len(L[0])):
                for kier in range(4):
                    for vel in range(3):
                        if minimum>Dist[y][x][kier][vel] and Proc[y][x][kier][vel] is False:
                            minimum=Dist[y][x][kier][vel]
                            min_id=(y, x, kier, vel)
        if min_id is None:
            break
        y, x, kier, vel = min_id[0], min_id[1], min_id[2], min_id[3]
        #poniżej obroty:
        if kier==0 or kier==2:
            Dist[y][x][1][0]=min(Dist[y][x][1][0], Dist[y][x][kier][vel]+45)
            Dist[y][x][3][0]=min(Dist[y][x][3][0], Dist[y][x][kier][vel]+45)
        else:
            Dist[y][x][0][0]=min(Dist[y][x][0][0], Dist[y][x][kier][vel]+45)
            Dist[y][x][2][0]=min(Dist[y][x][2][0], Dist[y][x][kier][vel]+45)
        #poniżej ruch:
        if 0<=x+ruchy(kier)[0]<len(L[0]) and 0<=y+ruchy(kier)[1]<len(L) and L[y+ruchy(kier)[1]][x+ruchy(kier)[0]]!='X':
            if vel==0:
                Dist[y+ruchy(kier)[1]][x+ruchy(kier)[0]][kier][1]=min(Dist[y+ruchy(kier)[1]][x+ruchy(kier)[0]][kier][1], Dist[y][x][kier][vel]+60)
            elif vel==1:
                Dist[y+ruchy(kier)[1]][x+ruchy(kier)[0]][kier][2]=min(Dist[y+ruchy(kier)[1]][x+ruchy(kier)[0]][kier][2], Dist[y][x][kier][vel]+40)
            else:
                Dist[y+ruchy(kier)[1]][x+ruchy(kier)[0]][kier][2]=min(Dist[y+ruchy(kier)[1]][x+ruchy(kier)[0]][kier][2], Dist[y][x][kier][vel]+30)
        procd+=1
        Proc[y][x][kier][vel]=True
    minimum=inf
    for kier in range(4):
        for vel in range(3):
            minimum=min(minimum, Dist[B[1]][B[0]][kier][vel])
    if minimum==inf:
        return None
    return minimum

    
runtests( robot )


