def dfs(s,q,visit):
    visit[s] = 1
    for i in q[s]:
        if visit[i]==0:
            dfs(i,q,visit)
    return visit

N = int(input())

n = int(input())

visit = [0] * (N+1)
q = [[] for _ in range(N+1)]

for _ in range(n):
    a,b = map(int,input().split())
    q[a].append(b)
    q[b].append(a)
dfs(1,q,visit)
print(sum(visit)-1)