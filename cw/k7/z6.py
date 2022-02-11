'''
Proszę napisać funkcję wstawiającą na koniec listy nowy element. Do
funkcji należy przekazać wskazanie na pierwszy element listy oraz wstawianą
wartość.
'''
class Node:
    def __init__(self,val = None):
        self.val = val
        self.next = None

def push_front(first, val):
    q=Node(val)
    q.next=first
    return q

def push_back(first, val):
    prev=None
    p=first
    while(p!=None):
        prev=p.val
        p=p.next
    q=Node(val)
    if(prev==None):
        q.next=val
        return q
    prev.next=q
    q.next=None
    return q

def write(first):
    while(first!=None):
        print(first.val)
        first=first.next
    return

first=None
first=push_front(first, 3)
first=push_back(first, 4)
write(first)