T = int(input())

for tc in range(1,T+1):
    N , M = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]
    max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            for k in range(M):
                for h in range(M):
                    sum += data[i+k][j+h]
                    if sum > max:
                        max = sum
    print(f'#{tc} {max}')