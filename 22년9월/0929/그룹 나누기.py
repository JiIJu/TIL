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


T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    data = list(map(int,input().split()))
    p = [0] *(N+1)

    a = []
    for i in range(0,2*M,2):
        a.append([data[i],data[i+1]])
    for i in range(1,N+1):
        make_set(i)

    for i in range(M):
        union(a[i][0],a[i][1])
    for i in range(1,N+1):
        p[i] = find_set(i)
    ans = []

    for i in range(1,len(p)):
        if p[i] not in ans:
            ans.append(p[i])

    print(f'#{tc} {len(ans)}')
    # print(p)
    # print(ans)
