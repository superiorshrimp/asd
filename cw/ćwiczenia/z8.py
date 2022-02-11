import math
'''
def f(B, D, T): #przejazd z 0 do B z bakiem o pojemności D; T - tablica lokalizacji stacji benzynowych
    curr=0
    licznik=0
    index=0
    while True:
        flag=0
        while T[index]-curr<=D:
            flag=1
            index+=1
            if index==len(T):
                if B-curr<=D:
                    return licznik
                elif B-T[index-1]<=D:
                    return licznik+1
                else: 
                    return -1
        if flag==1:
            curr=T[index-1]
            licznik+=1
        else:
            return -1
D=7
T=[3, 5, 7, 11, 14]
print(f(21, D, T))
'''
'''
def f(B, D, T): #T=[ [lokalizacja stacji, koszt paliwa za litr], ... ]
    W=[[math.inf for j in range(D+1)] for i in range(len(T)+2)]
    T.insert(0,[0, math.inf])
    T.append([B, math.inf])
    W[0][D]=0
    for i in range(1,len(T)):
        for k in range(D+1):
            distance=T[i][0]-T[i-1][0]
            if k+distance<=D:
                W[i][k]=W[i-1][k+distance]
            for j in range(1,D-k+2):
                W[i][k]=min(W[i][k], W[i][k-j]+j*T[i][1])
    minimum=math.inf
    for el in W[len(T)-1]:
        minimum=min(minimum, el)
    return minimum

B=20
D=6
T=[[3,1], [6,2], [11,1], [16,2], [18,3]]
print(f(B, D, T))
'''