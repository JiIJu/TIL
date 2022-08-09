T = int(input())

for i in range(1,T+1):
    K,N,M = map(int,input().split())
    data = [0] * (N + K*10)
    Mdata = list(map(int,input().split()))
    for j in range(M):
        data[Mdata[j]] = 1
    n = 0
    count=0
    while n<N:
        for j in range(K,-1,-1):
            if j == 0:
                n = N
                count=0
                break
            elif data[n+j] == 1:
                n += j
                count+=1
                break
            elif n + j >= N:
                n += j
                break

    print(f'#{i} {count}')
