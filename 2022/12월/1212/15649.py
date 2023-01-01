# 15649 N과M

N , M = map(int,input().split())


ans = []

def solve():
    if len(ans)==M:
        print(*ans)
        return
    for i in range(1,N+1):
        if i in ans:
            continue
        ans.append(i)
        solve()
        ans.pop()
solve()