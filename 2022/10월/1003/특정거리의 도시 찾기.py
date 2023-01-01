def dijstra(s,V):
    U = [0]*(V+1)
    v[s] = 1
    U[s]=1
    for i in range(V+1):
        D[i] = adjM[s][i]

    for i in range(V+1):
        u = 0
        minv = 99999
        for j in range(V+1):
            if U[j]==0 and minv>D[j]:

                u = j
                minv = D[j]
        U[u] = 1

        for i in range(V+1):
            if 0<adjM[u][i]<99999:
                D[i] = min(D[i],D[u]+adjM[u][i])



# N:도시수 M:도로수 K:거리정보 X:출발도시
N,M,K,X = map(int,input().split())
INF = 999
adjM = [[] for _ in range(N+1)]
v = [0]*[N+1]
for i in range(M):
    s,g = map(int,input().split())
    adjM[s].append((g,1))
print(adjM)
D = [0]*(N+1)
dijstra(X,N)
if K not in D:
    print(-1)
else:
    for i in range(1,N+1):
        if D[i]==K:
            print(i)