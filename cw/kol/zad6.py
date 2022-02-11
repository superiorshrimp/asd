#Szymon Żychowicz

'''
braklo czasu, ale probowalem poki pierwsze elemenety sa rowne dodawac je do nowej listy, potem przechodzac po liscie az ktoras z 3 sie skonczy
jak ktoras sie skonczy stworzylbym uproszczona wersje funkcji iloczyn ktora robila by iloczyn dla 2 zbiorow ale juz braklo czasu
'''

class Node:
    def __init__(self, val=None):
        self.val=val
        self.next=None

def najmniejsza(a,b,c): #zwraca najmniejsza wartosc z 3
    if(a<b):
        if(a<c):
            return a
        else:
            return c
    else:
        if(b<c):
            return b
        else:
            return c

def iloczyn_dwoch(zbior1, zbior2):
    if(zbior1 is None):
        return zbior2
    elif(zbior2 is None):
        return zbior1
    
def iloczyn(zbior1,zbior2,zbior3):
    if(zbior1 is None):
        if(zbior2 is None):
            return zbior3
        return iloczyn_dwoch(zbior2, zbior3)
    elif(zbior2 is None):
        return iloczyn_dwoch(zbior1, zbior3)
    nowa=None
    if(zbior1.val==zbior2.val==zbior3.val):
        nowa=Node(zbior1.val)
        zbior1=zbior1.next
        zbior2=zbior2.next
        zbior3=zbior3.next
        prev=nowa
        while(zbior1 is not None and zbior2 is not None and zbior3 is not None and zbior1.val==zbior2.val==zbior3.val):
            zb=Node(zbior1.val)
            prev.next=zb
            prev=prev.next
            zbior1=zbior1.next
            zbior2=zbior2.next
            zbior3=zbior3.next
    if(zbior1 is None):
        if(zbior2 is None):
            dodaj=zbior3
            nowa.next=dodaj
            return nowa
        dodaj=iloczyn_dwoch(zbior2, zbior3)
        nowa.next=dodaj
        return nowa
    elif(zbior2 is None):
        dodaj=iloczyn_dwoch(zbior1, zbior3)
        nowa.next=dodaj
        return nowa
    #TODO: nexty sa puste
    prev1=zbior1
    prev2=zbior2
    prev3=zbior3
    curr1=zbior1.next
    curr2=zbior2.next
    curr3=zbior3.next
    while(curr1 is not None and curr2 is not None and curr3 is not None):
        if(curr1.val==curr2.val==curr3.val):
            if(nowa is None):
                nowa=Node(curr1.val)
                prev=nowa
            else:
                zb=Node(curr1.val)
                prev.next=zb
            prev1=curr1
            prev2=curr2
            prev3=curr3
            curr1=curr1.next
            curr2=curr2.next
            curr3=curr3.next
        elif(curr1.val==najmniejsza(curr1.val, curr2.val, curr3.val)):
            prev1=curr1
            curr1=curr1.next
        elif(curr2.val==najmniejsza(curr1.val, curr2.val, curr3.val)):
            prev2=curr2
            curr2=curr2.next
        else:
            prev3=curr3
            curr3=curr3.next
    #w tym miejscu ktorys ze zbiorow jest pusty
    if(curr1 is None):
        if(curr2 is None):
            dodaj=curr3
            nowa.next=dodaj
            return nowa
        dodaj=iloczyn_dwoch(curr2, curr3)
        nowa.next=dodaj
        return nowa
    elif(curr2 is None):
        dodaj=iloczyn_dwoch(curr1, curr3)
        nowa.next=dodaj
        return nowa
        