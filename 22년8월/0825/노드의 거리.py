def bfs(road,S,G):
    visited = [0] * (V+1)
    queue = []
    check = [0] * (V+1)
    queue.append(S)
    check[S] =0
    visited[S] = 1
    while queue:

        t = queue.pop(0)

        for i in road[t]:
            if visited[i] != 1:
                queue.append(i)
                check[i] = check[t]+ 1
                visited[i] = 1


        if visited[G] == 1:
            return check[G]
    return 0



T = int(input())

for tc in range(1,T+1):
    V , E = map(int,input().split())

    road = [list(map(int,input().split())) for _ in range(E)]
    S,G = map(int,input().split())
    data = [[] for _ in range(V+1)]
    for i in range(E):
        data[road[i][0]].append(road[i][1])
        data[road[i][1]].append(road[i][0])

    print(f'#{tc} {bfs(data,S,G)}')


