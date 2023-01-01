T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = []
    for i in range(N):
        data.append([])
        data[i].append(1)
    for i in range(1,N):
        for j in range(i):
            data[i].append(1)
    for i in range(1,N):
        for j in range(1,N):
            if 1<=j<N-1 and i >=2 and j<i:
                data[i][j] = data[i-1][j] + data[i-1][j-1]
    print(f'#{tc}')
    for i in range(N):
        print(*data[i])