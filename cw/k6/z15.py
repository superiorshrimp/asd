'''
Problem 8 Hetmanów (treść oczywista)
'''
'''
def czy_mozna(i, j):
    global T
    if(k[i]==1):
        return False
    if(w[i]==1):
        return False
    if(p1[j-i]==1)

def f(N, i, j):
    if(i==7):
        for j in range(N):
            if(czy_mozna(i, j)==True):
                return True
    for j in range(N):
        if(i+1<N):
            if(czy_mozna(i+1, j
                f(N, i+1, j)
N=8
T=[[0 for j in range(N)] for i in range(N)]

for j in range(N):
    f(TR, 0, j)
'''
def czy_mozna(T, y, x):
    for i in range(len(T)):
        if(i!=y and T[i][x]==1):
            return False
    for j in range(len(T)):
        if(j!=x and T[y][j]==1):
            return False
    i, j = 1, 1
    while(x-j>=0 and y-i>=0):
        if(T[y-i][x-j]==1):
            return False
        i+=1
        j+=1
    i, j = 1, 1
    while(x+j<len(T) and y+i<len(T)):
        if(T[y+i][x+j]==1):
            return False
        i+=1
        j+=1
    return True

def f(T, i, j):
    print("a",i,j)
    if(i==len(T)):
        print("tag")
        for a in range(len(T)):
            print(T[a][:])
        exit(0)
        return True
    for k in range(len(T)):
        TC=[[T[p][l] for l in range(len(T))] for p in range(len(T))]
        if(czy_mozna(TC, i, k)==True):
            TC[i][k]=1
            f(TC, i+1, k)
    return

N=8
T=[[0 for j in range(N)] for i in range(N)]
TC=[[T[p][k] for k in range(len(T))] for p in range(len(T))]
for j in range(N):
    print(f(T, 0, j))