def qsort(A,l,r):
    if l<r:
        s = partition(A,l,r)
        qsort(A,l,s-1)
        qsort(A,s+1,r)


def partition(A,l,r):
    p = A[l]
    i, j = l,r
    while i<=j:
        while i<=j and A[i]<=p:
            i+=1
        while i<=j and A[j]>=p:
            j-=1
        if i<j:
            A[i],A[j] = A[j],A[i]
    A[l] , A[j] = A[j] , A[l]
    return j

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    A = list(map(int,input().split()))

    qsort(A,0,N-1)
    print(f'#{tc} {A[N//2]}')