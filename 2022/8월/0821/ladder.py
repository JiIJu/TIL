for tc in range(1,11):
    N = int(input())
    data = [[0] + list(map(int,input().split())) + [0] for _ in range(100)]
    n = 99
    m = 0
    k= 0
    for i in range(101):
        if data[99][i] == 2:
            m = i

    dn = [-1,0,0] #상좌우
    dm = [0,1,-1]
    while True:
        if n ==0:
            break
        if data[n][m-1] == 1:
            k = 2
            while True:
                n += dn[k]
                m += dm[k]
                if data[n][m-1]==0:
                    break
        elif data[n][m+1] ==1:
            k=1
            while True:
                n += dn[k]
                m += dm[k]
                if data[n][m+1]==0:
                    break

        k = 0

        n += dn[k]
        m += dm[k]

    print(f'#{tc} {m-1}')



