'''
Dana jest tablica T[N]. Proszę napisać program zliczający liczbę “enek” o określonym iloczynie
enka-n liczb wymnozonych przez siebie
'''
'''
def f(q, T, i, n):
    global licznik
    if(q!=1 and i==len(T)):
        return
    if(q==1):
        licznik.append(n)
        return 
    if(q%T[i]==0):
        f(q//T[i], T, i+1, n+1)
        f(q, T, i+1, n)
    else:
        f(q, T, i+1, n)
    
licznik=[]
T=[1, 3, 5, 15, 8743, 983]
print(f(15, T, 0, 0))

print(licznik)
'''
cnt = 0
def func(il,T,nki,i=0):
    global cnt
    if i == len(T)-1 or nki == 0:
        if il == 1:
            cnt += 1
            return True
        else:
            return False
    if il % T[i] == 0:
        return func(il//T[i],T,nki-1,i+1)|func(il,T,nki,i+1)
    else:
        return func(il,T,nki,i+1)
T = [1,2,3,4,5,6]
func(12,T,3)
print(cnt)