T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = list(map(int, input().split()))
    for i in range(N):
        for j in range(N-i-1):
            if data[j]>data[j+1]:
                data[j] , data[j+1] = data[j+1] , data[j]
    a = ''
    for i in range(N):

        a += ' ' + str(data[i])
    print(f'#{tc}{a}')