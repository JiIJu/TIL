
T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = list(map(int,input().split()))

    for i in range(N):
        for j in range(N-i-1):
            if data[j] > data[j+1]:
                data[j] , data[j+1] = data[j+1] , data[j]
    copy = []
    copy = data.copy()


    for i in range(0, N, 2):
        data[i] = copy[-(i+2)//2]

    for i in range(1,N,2):
        data[i] = copy[(i-1)//2]

    for i in range(N):
        s = ''
        for j in range(10):
            s += ' ' + str(data[j])
    print(f'#{tc}{s}')