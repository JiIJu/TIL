def MST_prim(r,V):
    MST = [0] * (V+1)
    key = [99999] * (V+1)
    key[r] = 0

    for i in range(V):
        u = 0
        min_v = 1111111
        for j in range(V+1):
            if MST[j] == 0 and key[j]<min_v:
                u = j
                min_v = key[j]
        MST[u] = 1

        for v in range(V+1):
            if MST[v] == 0 and a[u][v] > 0:
                key[v] = min(key[v] , a[u][v])
    print(key)
    return sum(key)

T = int(input())

for tc in range(1,T+1):
    V , E  = map(int,input().split())
    a = [[0]*(V+1) for _ in range(V+1)]

    for i in range(E):
        n1,n2,w = map(int,input().split())
        a[n1][n2] = w
        a[n2][n1] = w
    print(f'#{tc} {MST_prim(0,V)}')
