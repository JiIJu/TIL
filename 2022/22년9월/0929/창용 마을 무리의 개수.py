
def make_set(x):
    p[x] = x
    return
def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])

def union(x,y):
    p[find_set(y)] = find_set(x)
    return
T = int(input())

for tc in range(1,T+1):
    N , M = map(int,input().split())
    p = [0]* (N+1)

    for i in range(1,N+1):
        make_set(i)

    for i in range(M):
        x,y = map(int,input().split())
        union(x,y)
    for j in range(M):
        for i in range(N+1):
            p[i] = find_set(i)
            print(p[i])
    ans = []
    for i in range(1,N+1)
        if p[i] not in ans:
            ans.append(p[i])
    print(f'#{tc} {len(ans)}')