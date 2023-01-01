T = int(input())

for tc in range(1,T+1):
    N , K = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            count = 0
            if data[i][j] == 1 and (data[i][j-1] != 1 or j ==0):
                for k in range(N-j):
                    if data[i][j+k] ==1:
                        count+=1
                    else:
                        break
                if count == K:
                    result +=1
    for i in range(N):
        for j in range(N):
            count = 0
            if data[j][i] == 1 and (data[j-1][i] != 1 or j ==0):
                for k in range(N-j):
                    if data[j+k][i] ==1:
                        count+=1
                    else:
                        break
                if count == K:
                    result +=1



    print(f'#{tc} {result}')