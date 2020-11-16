#121910313016
a=list(map(int,input().split()))
def QuickSort(l):
    n=len(l)
    if n<2:
        return l
    cur=0
    for i in range(1,n):
        if l[i]<=l[0]:
            cur+=1
            l[cur],l[i]=l[i],l[cur]
    l[0],l[cur]=l[cur],l[0]
    left=QuickSort(l[0:cur])
    right=QuickSort(l[cur+1:])
    return left+[l[cur]]+right
print("Sorted array is ",QuickSort(a))
