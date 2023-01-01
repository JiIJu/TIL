T = int(input())

for tc in range(1,T+1):
    N , M = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]
    max = 0

    for i in range(N):
        count=0
        for j in range(M):
            if data[i][j] == 1:
                count +=1
            else:
                count=0
            if count>max:
                max=count
    for i in range(M):
        count=0
        for j in range(N):
            if data[j][i] == 1:
                count +=1
            else:
                count=0
            if count>max:
                max=count

    print(f'#{tc} {max}')