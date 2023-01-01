T = int(input())

for tc in range(1,T+1):
    N = int(input())

    data = [[] for _ in range(N)]

    for i in range(1,N+1):
        data[i-1] += [1] * i

    for i in range(N):
        for j in range(N):
            if i>=2 and j<i and 1<=j<N-1:
                data[i][j] = data[i-1][j-1] + data[i-1][j]
    print(f'#{tc}')
    for i in range(N):
        print(*data[i])
