def prim(r,V):
    MST = [0]*(V+1)
    key = [10000]*(V+1)

    key[r] = 1
    for i in range(V):
        u = 0
        minv=10000
        for j in range(V+1):
            if MST[j] == 0 and key[j]<minv:
                u = j
                minv = key[j]
        MST[u] = 1
        for v in range(V+1):
            if MST[v]==0 and 0<adj[u][v]:
                key[v] = min(minv,adjM[u][v])
    return sum(key)

def dijstra(s,V):
    U = [0]*(V+1)
    U[s] = 1
    for i in range(V+1):
        D[i] = adjM[s][i]

    for i in range(V):
        u = 0
        minv = 99999
        for j in range(V+1):
            if U[j]==0 and minv>D[j]:
                minv = D[j]
                u = j
    U[u] = 1
    for v in range(V+1):
        if 0<adjM[u][v]<99999:
            D[v] = min(D[v],D[u]+adjM[u][v])

V,E = map(int,input().split())
adjM = [[9999]*(V+1) for _ in range(V+1)]

for i in range(V+1):
    adjM[i][i] = 0
D = [0]*(V+1)