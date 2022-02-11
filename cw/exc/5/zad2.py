from copy import deepcopy

class NIEkarta:
    def __init__(self,cena,wartosc):
        self.cena = cena
        self.wartosc = wartosc

def starszy_pasjonat(T,x,D):
    F=[ [ [ 0 for j in range(x+1)] for k in range(D+1)] for i in range(len(T))]
    Prev=[ [ [ (None, None, None) for j in range(x+1)] for k in range(D+1)] for i in range(len(T))]
    F[0][T[0].cena][1]=T[0].wartosc
    max_id=(0,T[0].cena,1)
    maksimum=T[0].wartosc
    for i in range(1,len(T)):
        if T[i].cena<=D:
            F[i][T[i].cena][1]=T[i].wartosc
            if T[i].wartosc>maksimum:
                maksimum=T[i].wartosc
                max_id=(i, T[i].cena, 1)
        for k in range(D+1):
            for j in range(1,x+1):
                F[i][k][j]=F[i-1][k][j]
                Prev[i][k][j]=(i-1,k,j)
                if k-T[i].cena>=0 and F[i-1][k-T[i].cena][j-1]!=0:
                    if F[i][k][j]<F[i-1][k-T[i].cena][j-1]+T[i].wartosc:
                        F[i][k][j]=F[i-1][k-T[i].cena][j-1]+T[i].wartosc
                        Prev[i][k][j]=(i-1, k-T[i].cena, j-1)
                        if F[i][k][j]>maksimum:
                            maksimum=F[i][k][j]
                            max_id=(i, k, j)
    Res=[]
    prev=-1
    while max_id[0] is not None:
        if max_id[2]!=prev:
            Res.append(max_id[0])
        prev=max_id[2]
        max_id=(Prev[max_id[0]][max_id[1]][max_id[2]][0], Prev[max_id[0]][max_id[1]][max_id[2]][1], Prev[max_id[0]][max_id[1]][max_id[2]][2]) 
    return Res[::-1]

T = [NIEkarta(5,10), NIEkarta(5,5), NIEkarta(9,1), NIEkarta(10,2)]
cp = deepcopy(T)
x = 2
D = 10
print(starszy_pasjonat(T,x,D),[cp[0],cp[1]])

T = [NIEkarta(5,10), NIEkarta(2,5), NIEkarta(4,6), NIEkarta(1,2)]
cp = deepcopy(T)
x = 3
D = 9
print(starszy_pasjonat(T,x,D),[cp[0],cp[1],cp[-1]])