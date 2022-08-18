T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = list(map(int,input().split()))
    max = data[-1]
    a = len(data)

    sum = 0
    for i in range(a-1,-1,-1):
        if data[i]>max:
            max = data[i]
        else:
            sum += max-data[i]

    if sum == 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {sum}')
