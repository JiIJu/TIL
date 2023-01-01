def comb(n,r):
    global min
    if r==0:
        height = B-sum(tmp)

        if sum(tmp)>=B and abs(height)<=min:
            min = abs(height)

    elif n<r:
        return
    else:
        tmp[r-1] = H[n-1]
        comb(n-1,r-1)
        comb(n-1,r)


T = int(input())

for tc in range(1,T+1):
    N , B = map(int,input().split())
    H = list(map(int,input().split()))

    data = []
    tmp = [0]*N
    min = 99999

    for i in range(1,N+1):
        comb(N,i)


    print(f'#{tc} {min}')
    # for i in range(N):
