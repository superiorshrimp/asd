from zad3testy import runtests

def heapify_min(T, i, size):
    l=2*i+1
    p=2*i+2
    minimum=i
    if l<size and T[i][0]>T[l][0]:
        minimum=l
    if p<size and T[minimum][0]>T[p][0]:
        minimum=p
    if minimum!=i:
        T[i], T[minimum] = T[minimum], T[i]
        heapify_min(T, minimum, size)

def build_heap(T):
    for i in range(len(T)//2, -1, -1):
        heapify_min(T, i, len(T))

def tasks(T):
    if len(T)==1:
        return T[0]
    heap=[(T[i].val, i) for i in range(len(T))]
    build_heap(heap)
    head=T[heap[0][1]]
    T[heap[0][1]]=head.next
    if head.next is not None:
        heap[0]=(head.next.val, heap[0][1])
    else:
        heap[0]=heap[len(heap)-1]
        del heap[len(heap)-1]
    heapify_min(heap, 0, len(heap))
    head.next=None
    curr=head
    while len(heap)!=0:
        new=T[heap[0][1]]
        T[heap[0][1]]=new.next
        curr.next=new
        if new.next is not None:
            heap[0]=(new.next.val, heap[0][1])
        else:
            heap[0]=heap[len(heap)-1]
            del heap[len(heap)-1]
        heapify_min(heap, 0, len(heap))
        new.next=None
        curr=new
    return head

runtests( tasks )
