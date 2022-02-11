class Node:
    def __init__(self, val, next):
        self.val=val
        self.next=next

def utworz_linkliste_z_listy(T):
    if(len(T)==0):
        return None
    zbior=Node(T[0], None)
    kopia=zbior
    for k in T[1:]:
        nowy=Node(k, None)
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

def insertion_sort_node(head):
    curr=head.next
    prev=head
    i=1
    while curr is not None:
        if curr.val<head.val:
            prev.next=curr.next
            curr.next=head
            head=curr
            curr=prev
        else:
            j=1
            copy=head.next
            copy_prev=head
            while curr.val>copy.val and j<i:
                j+=1
                copy_prev=copy
                copy=copy.next
            if j!=i:
                prev.next=curr.next
                curr.next=copy
                copy_prev.next=curr
                curr=prev
        i+=1
        prev=curr
        curr=curr.next
    return head

def merge_sorted_nodes(head1, head2):
    if head1 is None:
        return head2
    elif head2 is None:
        return head1
    if head1.val>head2.val:
        head2, head1 = head1, head2
    curr1=head1.next
    prev1=head1
    while curr1 is not None and head2 is not None:
        if curr1.val>head2.val:
            new=head2
            head2=head2.next
            prev1.next=new
            new.next=curr1
            prev1=new
        else:
            prev1=curr1
            curr1=curr1.next
    if curr1 is None:
        prev1.next=head2
    return head1

def rek(head, length): #potrzebne do powyższej i poniższej funkcji do merge sortu
    if length==1:
        return head
    head1=head
    prev=None
    for i in range(length//2):
        prev=head
        head=head.next
    prev.next=None
    head2=head
    len1=length//2
    len2=length-length//2
    return merge_sorted_nodes(rek(head1,len1), rek(head2,len2))

def merge_sort_node(head):
    len=0
    curr=head
    while curr is not None:
        curr=curr.next
        len+=1
    return rek(head, len)

#uwaga z tymi poniżej

def push(head, new, tail): #dopina element na poczatek, zapamietujac tail
    if head is None:
        new.next=None
        return new, new
    new.next=head
    return new, tail

def quicksort(head): #Node
    if head is None or head.next is None:
        return head, head
    else:
        pivot=head.val
        curr=head.next
        head.next=None
        h1, t1, heq, teq, h2, t2 = None, None, head, head, None, None
        while curr is not None:
            tmp=curr.next
            if curr.val<pivot:
                h1, t1 = push(h1, curr, t1)
            elif curr.val>pivot:
                h2, t2 = push(h2, curr, t2)
            else:
                heq, teq = push(heq, curr, teq)
            curr=tmp
    h1,t1=quicksort(h1)
    h2,t2=quicksort(h2)
    if h1 is not None:
        t1.next=heq
        if h2 is not None:
            teq.next=h2
            return h1, t2
        else:
            return h1, teq
    else:
        if h2 is not None:
            teq.next=h2
            return heq, t2
        else:
            return heq, teq

def qsort(head):
    return quicksort(head)[0]

