



T = int(input())

for tc in range(1,T+1):
    N , M =  map(int,input().split())
    data = []

    for i in range(N):
        data.append(list(map(int,input().split())))
    home = []
    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                home.append([i,j])
    # print(home)
    max= 0
    money = 0
    cnt = 0
    for i in range(N):
        for j in range(N):

            for k in range(1,N+5):
                cnt = 0
                # if data[i][j] == 1:
                #     cnt += 1
                # for l in range(1,k):
                #     if k > 1 and 0 <= j + l < N and data[i][j + l] == 1:
                #         cnt += 1
                #     if k > 1 and 0 <= j - l < N and data[i][j - l] == 1:
                #         cnt += 1
                for a in range(k):
                    if 0 <= i + a < N and data[i + a][j] == 1:
                        cnt += 1
                    if a!=0 and 0 <= i - a < N and data[i - a][j] == 1:
                        cnt += 1
                    for l in range(1,k-a):
                        # if 0<=i+a<N and 0<=j+(l)<N and data[i+a][j] == 1:
                        #     cnt += 1
                        if 0<=i+a<N and 0<=j+(l)<N and data[i+a][j+(l)] == 1:
                            cnt += 1
                        if 0<=i+a<N and 0<=j-(l)<N and data[i+a][j-(l)] == 1:
                            cnt += 1
                        if a!=0 and 0<=i-a<N and 0<=j+(l)<N and data[i-a][j +(l)] == 1:
                            cnt += 1
                        if a!=0 and 0<=i-a<N and 0<=j-(l)<N and data[i-a][j-(l)] == 1:
                            cnt += 1
                K = k+1
                cost = (k * k + (k - 1) * (k - 1))
                money = (cnt) * M - cost
                # print([i,j],money , cnt , k,cost)
                if money>=0 and cnt>max:
                    max = cnt


    print(f'#{tc} {cnt}')


