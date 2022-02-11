'''
Zadanie 4. Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia pola szachownicy o
wymiarach NxN ruchem skoczka szachowego.
'''
'''
def kopia_dwuwymiarowej_tablicy(T1):
    T2=[[T1[i][j] for j in range(len(T1))] for i in range(len(T1))]
    return T2

def f(T, T1, x, y, pola):
    global stop
    if(stop==True):
        print("bruh")
        exit(0)
    TC=kopia_dwuwymiarowej_tablicy(T1)
    for i in range(len(TC)):
        print(TC[i][:])
    print("aaaaa")
    TC[y][x]=1
    if(pola==len(T)**2):
        print("bruh")
        stop=True
        exit(0)
    global ruchy
    for k in ruchy:
        if(x+k[1]<len(TC) and x+k[1]>=0 and y+k[0]<len(TC) and y+k[0]>=0 and TC[y+k[0]][x+k[1]]==0):
            TC[y+k[0]][x+k[1]]=1
            f(T, TC, x+k[1], y+k[0], pola+1)

stop=False
N=5
ruchy=((2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2))
T=[[0 for j in range(N)] for i in range(N)]
TC=kopia_dwuwymiarowej_tablicy(T)
for i in range(len(T)//2+1):
    for j in range(len(T)//2+1):
        TC[j][i]=1
        f(T, TC, j, i, 1)
        TC[j][i]=0

#idzie w nieskonczonosc
'''
def can_move(i, x, y, dl):
    ruchy=((2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2))
    if(x+ruchy[i][0]>0 and x+ruchy[i][0]<dl and y+ruchy[i][1]>0 and y+ruchy[i][1]<dl):
        return x+ruchy[i][0], y+ruchy[i][1]
    return -1, -1

def ruch(tab, counter, row, col):
    for i in range(8):
        x, y = can_move(i, row, col, len(tab))
        if(x!=-1 and y!=-1 and tab[x][y]!=True):
            tab[x][y]=counter
            if(ruch(tab, counter-1, x, y))==True:
                return True
            tab[x][y]=False
    return False
def start(num):
    counter=num**2
    for i in range(num):
        for j in range(num):
            tab=[[False for _ in range(num)] for _ in range(num)]
            tab[i][j]=counter
            return ruch(tab, counter, i, j)

print(start(8))
#zle