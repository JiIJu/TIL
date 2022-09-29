# def prim(r,N):
#     MST = [0]*(N+1)
#     key = [99999]*(N+1)
#     key[r] = 0
#
#     for i in range(N):
#         u = 0
#         minV = 99999
#         for j in range(N+1):
#             if MST[j] == 0 and minV>key[j]:
#                 u = j
#                 minV = key[j]
#         MST[u] = 1
#         for j in range(N+1):
#             if MST[j] == 0 and adjlist[u][j]>0:
#                 key[j] = min(key[j] ,adjlist[u][j])
#     print(key)
#     return sum(key)
#
#
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
    N , M ,X= map(int,input().split())
    adjlist = [[0]*(N+1) for _ in range(N+1)]

    for i in range(M):
        n1,n2,w = map(int,input().split())
        adjlist[n1][n2] = w

    max_V = 0
    # print(adjlist)
    D = [0] * (N + 1)
    dijkstra(2,N)
    print(D)

    # for i in range(1,N+1):
    #     D = [0] * (N + 1)
    #     dijkstra(i,N)
    #     a = D[X]
    #     print(D)
    #     D = [0] * (N + 1)
    #     dijkstra(X,N)
    #     print(D)
    #     b = D[i]
    #     print(a+b)
    #     if max_V<a+b:
    #         max_V = a+b
    # print(max_V)