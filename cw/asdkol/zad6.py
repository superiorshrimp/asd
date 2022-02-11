class Sum:
    def __init__(self, val):
        self.val=val

def DFS(T, x, y, Visited, ruchy, suma):
    for ruch in ruchy:
        if x+ruch[0]>=0 and x+ruch[0]<len(T[0]) and y+ruch[1]>=0 and y+ruch[1]<len(T) and Visited[y+ruch[1]][x+ruch[0]]==False and T[y+ruch[1]][x+ruch[0]]>0:
            Visited[y+ruch[1]][x+ruch[0]]=True
            suma.val+=T[y+ruch[1]][x+ruch[0]]
            DFS(T, x+ruch[0], y+ruch[1], Visited, ruchy, suma)

def plan(T):
    R=[]
    ruchy=((-1, 0), (1, 0), (0, 1), (0, -1))
    Visited=[[False for j in range(len(T[0]))] for i in range(len(T))]
    Ropa=[]
    for i in range(len(T[0])):
        if T[0][i]>0 and len(Ropa)!=0 and Ropa[len(Ropa)-1][1]==i-1:
            Ropa[len(Ropa)-1][1]=i
        if T[0][i]>0 and Visited[0][i]==False:
            Visited[0][i]=True
            suma=Sum(T[0][i])
            DFS(T, i, 0, Visited, ruchy, suma)
            Ropa.append([i, i, suma.val])
            del suma
    curr=0
    D=Ropa[0][2]
    idr=1
    add=0
    stop=0
    R.append(0)
    while True:
        if stop<10:
            print(curr, idr, D, R)
            exit(0)
        maks=0
        maks_index=-1
        for i in range(curr+1, curr+D+1):
            if i==len(T[0])-1:
                return R
            if idr<len(Ropa) and i>Ropa[idr][0]:
                idr+=1
            if idr<len(Ropa) and i==Ropa[idr][0]:
                q=D+Ropa[idr][2]-i+curr
                if q>maks:
                    add=Ropa[idr][2]-i+curr
                    maks_index=i
                    maks=q
        R.append(maks_index)
        D+=add
        curr=maks_index
        stop+=1
                
T=[[0 for j in range(16)] for i in range(5)]
T[0][0]=3
T[1][0]=4
T[0][3]=1
T[0][5]=3
T[0][7]=1
T[1][7]=2
T[2][7]=2
T[2][8]=1
plan(T)