def Dijkstra(s,N):
    U = [0]*(N+1)
    U[s]=1
    for i in range(N+1):
        D[i] = adjlist[s][i]

    for _ in range(N+1):
        u = 0
        minV = 99999
        for i in range(N+1):
            if U[i] == 0 and minV>D[i]:
                minV = D[i]
                u = i
        U[u] = 1
        for v in range(N+1):
            if 0<adjlist[u][v]<99999:
                D[v] = min(D[v],D[u]+adjlist[u][v])


T = int(input())

for tc in range(1,T+1):
    N,E = map(int,input().split())
    adjlist=[[99999]*(N+1) for _ in range(N+1)]
    for _ in range(E):
        s,g,w = map(int,input().split())
        adjlist[s][g] = w
    D = [0] * (N+1)


    Dijkstra(0,N)

    print(f'#{tc} {D[N]}')