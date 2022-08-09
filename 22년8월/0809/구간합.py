T = int(input())

for a in range(1,T+1):
    N , M = map(int,input().split())
    ai = list(map(int,input().split()))
    data=[0]*(N-M+1)
    for i in range(N-M+1):
        for j in range(M):
            data[i] += ai[i+j]

    for i in range(len(data)):
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j] , data[j+1] = data[j+1] , data[j]
    print(f'#{a} {data[-1]-data[0]}')
