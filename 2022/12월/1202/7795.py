#먹을것인가 먹힐것인가

T = int(input())

for tc in range(T):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int, input().split()))
    B.sort()
    A.sort()
    cnt=0

    for i in A:
        start = 0
        end = M-1
        while start<=end:
            mid = (start+end)//2
            if B[mid]>=i:
                end = mid-1
            else:
                start=mid+1
        
        cnt+=(start)
    print(cnt)
