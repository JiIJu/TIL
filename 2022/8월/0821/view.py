for tc in range(1,11):
    N = int(input())
    data = list(map(int,input().split()))
    count = 0
    for i in range(2,N-2):
        if data[i] > data[i-1] and data[i] > data[i-2] and data[i] > data[i+1] and data[i] > data[i+2]:
            a = [data[i-2],data[i-1],data[i+1],data[i+2]]
            max = 0
            for j in range(4):
                if a[j]>max:
                    max = a[j]
            count += data[i]-max
    print(f'#{tc} {count}')
