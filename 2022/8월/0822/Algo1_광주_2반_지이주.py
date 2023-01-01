T = int(input())

for tc in range(1,T+1):
    N = int(input())
    a = list(map(int,input().split()))

    data = [list(map(int,input().split())) for _ in range(N)]
    sum = 0
    avg = 0
    count = 0
    for i in range(a[0],a[2]+1): #평균을 구하기 위해 높이값의 합과 땅의 개수를 구한다.
        for j in range(a[1],a[3]+1):
           sum += data[i][j]
           count +=1
    avg = sum//count #평균을 계산

    cnt = 0


    for i in range(a[0],a[2]+1): #녹색의 영역중 평균보다 작거나 큰 값이 있으면 그 차이만큼 cnt에 더한다.
        for j in range(a[1],a[3]+1):
            if data[i][j]-avg>=1:
                cnt+=(data[i][j]-avg)
            elif data[i][j]-avg<=-1:
                cnt+=(avg-data[i][j])

    print(f'#{tc} {cnt}')
