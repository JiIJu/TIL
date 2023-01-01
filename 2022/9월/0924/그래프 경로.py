def dfs(S,G):
    # top = -1
    visited[S] = 1
    # print(S)
    while True:
        for w in data[S]:
            if visited[w] == 0:
                # top +=1
                stack.append(w)
                S = w
                # print(S)
                visited[w] = 1
                break
        else:
            if stack:
                S = stack.pop()
            else:
                break

T = int(input())

for tc in range(1,T+1):
    V , E = map(int,input().split())
    data = [[] for _ in range(V+1)]
    for _ in range(E):
        a , b = map(int,input().split())
        data[a].append(b)
        # data[b].append(a)
    # print(data)
    S,G = map(int,input().split())
    stack = []

    visited = [0] * (V+1)

    dfs(S,G)
    # print(visited)
    if visited[G]==1:
        print(f'#{tc} 1')
    elif visited[G]==0:
        print(f'#{tc} 0')