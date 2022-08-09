1일차 6차시 min max
T = int(input())

for i in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input().split()))

    for j in range(N):
        for k in range(N-j-1):
            if ai[k] >= ai[k + 1]:
                ai[k], ai[k+1] = ai[k+1], ai[k]
    print(f'#{i} {ai[N-1] - ai[0]}')