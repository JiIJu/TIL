def dijkstra(s,N):

    check = [0] * (N+1)
    for i in range(N+1):
        D[i] = adjlist[s][i]

    for _ in range(N+1):
        minV = 9999999
        u = 0
        for i in range(N+1):
            if check[i]==0 and minV>D[i]:
                minV = D[i]
                u = i
        check[u] = 1
        for i in range(N+1):
            if 0<adjlist[u][i]<999999:
                D[i] = min(D[i],D[u]+adjlist[u][i])


T = int(input())

for tc in range(1,T+1):
    N,E = map(int,input().split())
    adjlist=[[99999]*(N+1) for _ in range(N+1)]
    for _ in range(E):
        s,g,w = map(int,input().split())
        adjlist[s][g] = w
    D = [0] * (N + 1)
    dijkstra(0,N)
    print(D)