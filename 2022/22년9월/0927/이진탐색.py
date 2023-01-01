def qsort(A,l,r):
    if l<r:
        s = partition(A,l,r)
        qsort(A,l,s-1)
        qsort(A,s+1,r)


def partition(A,l,r):
    p = A[l]
    i,j = l,r
    while i<=j:
        while i<=j and A[i]<=p:
            i+=1
        while i<=j and A[j]>=p:
            j-=1
        if i<j:
            A[i],A[j] = A[j] , A[i]
    A[l],A[j] = A[j],A[l]
    return j

def binarySearch(n,S,key):
    global cnt
    low = 0
    high = n-1
    direction = 0
    while low <= high:
        mid = (high+low)//2
        if S[mid] == key:
            cnt +=1
            return
        elif S[mid]>key:
            if direction ==1:
                return
            direction = 1
            high = mid-1
        else:
            if direction==2:
                return
            direction = 2
            low = mid+1
    return

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    N_list = list(map(int,input().split()))
    M_list = list(map(int,input().split()))
    # qsort(N_list,0,N-1)
    # qsort(M_list,0,M-1)
    N_list = sorted(N_list)
    M_list = sorted(M_list)

    ans = []
    cnt = 0

    for i in range(M):
        binarySearch(N,N_list,M_list[i])
    print(f'#{tc} {cnt}')

