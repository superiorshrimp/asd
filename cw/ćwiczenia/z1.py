'''
def szukanie_sumy(T, suma):
    l=0
    p=len(T)-1
    while(l<p):
        if(T[l]+T[p]==suma):
            return True
        elif(T[l]+T[p]>suma):
            p-=1
        else:
            l+=1
    return False

T=[10, 15, 25, 56, 78, 89, 100]
print(szukanie_sumy(T, 107))
'''
'''
def fun(T):
    if(len(T)==0):
        return
    elif(len(T)==1):
        return T[0], T[0]
    else:
        if(T[0]<T[1]):
            min=T[0]
            max=T[1]
        else:
            min=T[1]
            max=T[0]
        i=2
        while(i+1<len(T)):
            if(T[i]<T[i+1]):
                if(T[i]<min):
                    min=T[i]
                if(T[i+1]>max):
                    max=T[i+1]
            else:
                if(T[i+1]<min):
                    min=T[i+1]
                if(T[i]>max):
                    max=T[i]
            i+=2
        if(i+1==len(T)):
            print("a")
            if(T[i]<min):
                min=T[i]
            elif(T[i]>max):
                max=T[i]
    return min, max

T=[10, 15, 25, 56, 78, 89, 100]
print(fun(T))
'''