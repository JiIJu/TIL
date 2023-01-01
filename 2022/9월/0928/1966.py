
T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    data = list(map(int,input().split()))
    find = data[M]
    cnt = 0
    stack = []
    n = 0
    i=0
    for i in range(N):
        if data[i]>find:
            M-=1
            if data[0]<find:
                M-=1
        if i==N:
            break
    print(M+1)

