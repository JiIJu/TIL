T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = list(map(int,input().split()))
    data_len = 0
    count = 0
    for i in data:
        data_len +=1

    for i in range(data_len-1):
        if data[i] == 1 and data[i+1] == 1:
            count +=1
    print(f'#{tc} {count}')