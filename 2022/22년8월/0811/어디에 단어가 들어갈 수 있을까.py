T = int(input())

for tc in range(1,T+1):
    N , K = map(int,input().split())

    data = [list(map(int,input().split())) for _ in range(N)]
    count = 0

    for i in range(N):
        result = 0
        for j in range(N):
            if data[i][j] == 1:
                result += 1
            elif data[i][j]==0 and result ==K:
                count+=1
                result = 0
            # elif j == N-1 and data[i][-1]==1 and result == K-1:
            #     count+= 1
            #     result =0
            elif data[i][j] == 0:
                result = 0
        if result == K:
            count +=1
    print(count)
    for i in range(N):
        result = 0
        for j in range(N):
            if data[j][i] == 1:
                result += 1
            elif data[j][i] == 0 and result ==K:
                count += 1
                result = 0
            # elif i == N-1 and data[j][-1]==1 and result == K-1:
            #     count+= 1
            #     result =0
            elif data[j][i]==0:
                result = 0
        if result == K:
            count +=1

    print(f'#{tc} {count}')