T = int(input())

for tc in range(1,T+1):
    N , Q = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(Q)]

    box = [0] * (N+1)

    for i in range(Q):
        for k in range(data[i][0],data[i][1]+1):
            box[k] = i+1
    a= ''
    for i in range(1,N+1):
        a += f' {box[i]}'
    print(f'#{tc}{a}')


