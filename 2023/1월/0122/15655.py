# N과M (6)

N,M = map(int,input().split())
data = list(map(int,input().split()))
data.sort()
a = []
def solve():
    if len(a)==M:
        if sorted(a)==a:
            print(*a)
        return
    for i in range(N):
        if data[i] not in a:
            a.append(data[i])
            solve()
            a.pop()
solve()