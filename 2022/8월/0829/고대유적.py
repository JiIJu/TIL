T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    max=0
    for i in range(N):
        cnt = 0
        for j in range(M):
            if arr[i][j]:
                cnt+=1
                if max<cnt:
                    max = cnt
            else:
                cnt = 0

    for i in range(M):
        cnt = 0
        for j in range(N):
            if arr[j][i]:
                cnt+=1
                if max<cnt:
                    max = cnt
                else:
                    cnt = 0
    print(f'#{tc} {max}')