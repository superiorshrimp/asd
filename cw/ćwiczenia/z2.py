'''
#zad3
#A[i1]+A[i2]=A[j1]+A[j2]
#N^3
def find_sum(A):
    if(len(A)<4):
        return False
    for pocz in range(len(A)-1):
        for kon in range(pocz+1, len(A))
            x=A[pocz]+A[kon]
            i=pocz+1
            j=kon-1
            while(i<j):
                if(x>A[i]+A[j]):
                    i+=1
                elif(x<A[i]+A[j]):
                    j-=1
                else:
                    return True
    return False

T=[1,2,3,4]
print(find_sum(T))
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

def merge_sorted_nodes(head1, head2): #jeśli elementy mogą się powtarzać w scalonym nodzie
    global licznik
    if head1 is None:
        return head2
    elif head2 is None:
        return head1
    if(head1.val<head2.val):
        new=head1
        head1=head1.next
    else:
        licznik+=1
        new=head2
        head2=head2.next
    curr=new
    while head1 is not None and head2 is not None:
        if(head1.val<head2.val):
            curr.next=head1
            head1=head1.next
        else:
            licznik+=1
            curr.next=head2
            head2=head2.next
        curr=curr.next
    if head1 is None:
        curr.next=head2
        while head2 is not None:
            licznik+=1
            head2=head2.next
    else:
        curr.next=head1
    return new


def scalanie_serii_normalnych(head):
    curr=head
    head1=head
    head2=None
    while curr is not None and curr.next is not None:
        if(curr.val>curr.next.val):
            tmp=curr
            curr=curr.next
            tmp.next=None
            head2=curr
            break
        else:
            curr=curr.next
    while curr is not None and curr.next is not None:
        if(curr.val>curr.next.val):
            tmp=curr
            curr=curr.next
            tmp.next=None
            head1=merge_sorted_nodes(head1, head2)
            head2=curr
        else:
            curr=curr.next
    if head2 is not None:
        return merge_sorted_nodes(head1, head2)
    return head1

licznik=0
head=None
head=utworz_linkliste_z_listy([1,5,10,2,3,8,11,10,57])
head=scalanie_serii_normalnych(head)
wypisz(head)
print(licznik)
'''
'''
def lider_ciagu(T):
    if len(T)==0:
        return False
    lider=T[0]
    licznik=1
    for i in range(1,len(T)):
        if licznik==0:
            lider=T[i]
            licznik=1
        else:
            if lider==T[i]:
                licznik+=1
            else:
                licznik-=1
    if licznik<=0:
        return False
    licznik=0
    for i in range(len(T)):
        if lider==T[i]:
            licznik+=1
    if licznik>len(T)//2:
        return True #mozna zwrocic index lidera, bo jest znany
    else:
        return False

#print(lider_ciagu([1,2,3]))
'''
'''
def quick_sort_y(T): #rekurencyjnie
    if(len(T)<=1):
        return T
    less=[]
    more=[]
    equal=[T[0]]
    compare=T[0][1][1]
    for i in range(1,len(T)):
        if(T[i][1][1]<compare):
            less.append(T[i])
        elif(T[i][1][1]==compare):
            equal.append(T[i])
        else:
            more.append(T[i])
    return quick_sort_y(less)+equal+quick_sort(more)

def quick_sort_y_top(T): #lepiej zrobic scalanie dla nowego elementu/ow
    if(len(T)<=1):
        return T
    less=[]
    more=[]
    equal=[T[0]]
    compare=T[0][1][1]
    for i in range(1,len(T)):
        if(T[i][0][1]<compare):
            less.append(T[i])
        elif(T[i][0][1]==compare):
            equal.append(T[i])
        else:
            more.append(T[i])
    return quick_sort_y(less)+equal+quick_sort(more)

def f(T, k): #T=[((x0, y0), (x1, y1)), ((x2, y2), (x3, y3)), ...]; k-ilosc wody
    T=quick_sort_y(T) #sortowanie po najmniejszym y
    licznik=0
    zapelnione=0
    podstawa=0
    Level=[]
    for i in range(len(T)):
        Level.append(T[i])
        podstawa+=T[i][1][0]-T[i][0][0]
        Level=quick_sort_y_top(Level)
        podstawa+=abs(T[i][0][1]-T[i][1][1])
        j=i+1
        while(j<len(T)):
            if(T[i][1][1]==T[j][1][1]):
                podstawa+=T[j][1][0]-T[j][0][0]
                Level.append(T[j])
                Level=quick_sort_y_top(Level)
                j+=1
            else:
                break    
        j-=1
        i=j
        if(i+1<len(T)):
            if(Level[0][0][1]<T[i+1][1][1]):
                zapelnione+=podstawa*abs(Level[0][0][1]-last)
                if(zapelnione>k):
                    return licznik
                else:
                    



    
        


T=[((-3,3),(-1,1)), ((-4,5),(-2,2)), ((0,3),(2,0)), ((-1,1),(1,-1))]
print(f(T, 10))






        if(T[i][1][1]<T[i+1][1][1]):
            zapelnione+=abs(T[i][0][1]-T[i][1][1])*abs(T[i][1][0]-T[i][0][0])
            if(zapelnione>k):
                return licznik
            elif(zapelnione==k):
                return licznik+1
        else:
            Level=[T[i], T[i+1]]
            j=i+2
            while(j<len(T)):
                if(T[i][1][1]==T[j][1][1]):
                    Level.append(T[j])
                    j+=1
                else:
                    break
        i=j-1
        
#nieskonczone
'''