def bfs(s,N):
    top = -1
    print(s)
    visited[s] = 1
    while True:
        for w in adjList[S]:
            top +=1 #push(s)
            stack[top] = s
            s = w #w에 방문
            print(w)
            visited[w] = 1
            break
        else:
            if top!=-1: # 스택이 비어있지 않은경우
                v = stack[top] # pop
                top -=1
            else:
                break
V, E = map(int, input().split())
N = V + 1
adjList = [[] for _ in range(N)]
# print(adjList)
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)
visited = [0] * N
stack = [0] * N
bfs(1,N)