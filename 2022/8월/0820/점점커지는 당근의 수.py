T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = list(map(int,input().split()))
    count = 1
    max = 0
    for i in range(N-1):
        if data[i]<data[i+1]:
            count+=1

        else:
            count=1
        if max < count:
            max = count
    print(f'#{tc} {max}')