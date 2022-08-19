T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]

    # print(data)
    rev = [[] for _ in range(N)]
    # for i in range(N):
    for j in range(N):
        a = ''
        b =''
        c = ''
        for k in range(1,N+1):
            a += str(data[N-k][j])
        for h in range(1,N+1):
            b += str(data[N-j-1][N-h])
        for l in range(0,N):
            c += str(data[l][N-j-1])
        rev[j].append(a)
        rev[j].append(b)
        rev[j].append(c)

    print(f'#{tc}')
    for i in range(N):
        print(*rev[i])