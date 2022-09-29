def prim(r,V):
    MST = [0]*(V+1)
    key = [99999]*(V+1)
    key[r] = 0

    for i in range(V):
        u = 0
        minV = 99999
        for j in range(V+1):
            if MST[j] == 0 and minV>key[j]:
                minV = key[j]
                u = j
        MST[u] = 1

        for j in range(V+1):
            if MST[j]==0 and a[u][j]>0:
                key[j] = min(key[j], a[u][j])
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

    print(prim(0,V))