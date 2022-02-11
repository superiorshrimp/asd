'''
#Lis - longest increasing subsequence (nie musi byc spojne)
def f(T):
    maks=0
    maks_id=0
    W=[[0,-1]]*len(T)
    for i in range(len(T)):
        max=0
        max_id=-1
        for j in range(i):
            if T[j]<=T[i] and W[j][0]>max:
                max=W[j][0]
                max_id=j
        W[i][0]=max+1
        if max+1>maks:
            maks=W[i][0]
            maks_id=max_id
        W[i][1]=max_id
    return maks, maks_id

T=[1,2,4,0,5,1,2,3]
print(f(T))
'''
'''
# knapsack
def f(P, W, k):
    maks=0
    T=[[0 for i in range(k+1)] for j in range(len(P))]
    start=0
    while W[start]>k:
        start+=1
    T[0][W[start]]=P[start]
    for i in range(start+1,len(P)):
        for j in range(k):
            T[i][j]=max(T[i-1][j], T[i][j])
            if j+W[i]<=k:
                T[i][j+W[i]]=max(T[i][j+W[i]], T[i-1][j]+P[i])
                maks=max(maks, T[i][j+W[i]])
    for el in T:
        print(el)
    return maks

P=[6, 3, 10, 11, 3, 2]
W=[5, 4, 7, 9, 3, 1]
print(f(P, W, 12))
'''
'''
def fu(P, W, k):
    maks=0
    suma=0
    w=0
    for i in range(len(P)):
        suma+=P[i]
        w+=W[i]
    T=[w for _ in range(suma+1)]
    start=0
    while start<len(P) and W[start]>k:
        start+=1
    if start<len(P):
        T[P[start]]=W[start]
        maks=P[start]
    for i in range(start+1,len(P)):
        for j in range(maks, -1, -1):
            if T[j]+W[i]<=k:
                T[j+P[i]]=min(T[j+P[i]], T[j]+W[i])
                maks=max(maks, j+P[i])
        T[P[i]]=min(T[P[i]], W[i])
        if T[P[i]]<=k:
            maks=max(maks, P[i])
    return maks
'''
'''
def f(T, k):
    W=[[0 for col in range(k+1)] for row in range(len(T))]
    start=0
    while T[start]>k:
        start+=1
    if T[start]==k:
        return 1
    W[0][T[start]]=1
    for i in range(1,len(T)):
        if T[i]<k:
            W[i][T[i]]=1
        elif T[i]==k:
            return 1
        for j in range(k):
            if W[i-1][j]==1:
                W[i][j]=1
                if j+T[i]<k: 
                    W[i][j+T[i]]=1
                elif j+T[i]==k:
                    return 1
    return 0

T=[6, 5, 3, 2, 5, 12]
print(f(T, 10))
'''
'''
#Lis - longest increasing subsequence (nie musi byc spojne); nlogn
def binary_search(T, start, stop, k):
    while start<stop:
        mid=(start+stop)//2
        if T[mid]<k:
            start=mid+1
        elif T[mid]>k:
            stop=mid-1
        else:
            return mid
    print(start, T[start], k)
    if T[start]>=k:
        return start
    else:
        return start+1
    

def f(T):
    maks=0
    H=[10000 for _ in range(len(T))]
    for i in range(len(T)):
        q=binary_search(H, 0, maks, T[i])
        print(q)
        maks=max(maks, q)
        H[q]=min(T[i], H[q])
        print(H)
    return maks+1

T=[1,2,4,7,5,1,2,0,3]
print(f(T))
'''
'''
#najdluzszy wspolny podciag; O(n^2)
def f(w1, w2):
    T=[[0 for j in range(len(w2))] for i in range(len(w1))]
    for i in range(len(w1)):
        if w1[i]==w2[0]:
            T[i][0]=1
    for i in range(len(w2)):
        if w2[i]==w1[0]:
            T[0][i]=1
    for i in range(1,len(w1)):
        for j in range(1,len(w2)):
            T[i][j]=max(T[i-1][j], T[i][j-1])
            if w1[i]==w2[j]:
                T[i][j]=max(1+T[i-1][j-1], T[i][j])

    for el in T:
        print(el)
    return T[len(w1)-1][len(w2)-1]
    
w1="abaabbaaa"
w2="babab"
print(f(w1, w2))
'''
