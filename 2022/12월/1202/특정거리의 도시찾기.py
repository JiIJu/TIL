# 이코테 특정거리의 도시찾기

def bfs(X):
    q = [X]
    while q:
        x = q.pop(0)
        for i in road[x]:
            if data[i]==-1:
                data[i] = data[x]+1
                q.append(i)


# N:도시수 M : 도로수 K:거리정 X : 출발도시정보
N , M , K , X = map(int,input().split())
road = [[] for _ in range(M+1)]
for i in range(M):
    a,b = map(int,input().split())
    road[a].append(b)
data = [-1]*(N+1)
data[X] = 0
bfs(X)

for i in range(1,N+1):
    if data[i] == K:
        print(i)
if K not in data:
    print(-1)