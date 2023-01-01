#15651 N과M (3)

N,M = map(int,input().split())
ans=[]
def solve():
    for i in range(1,N+1):
        if len(ans)==M:
            print(*ans)
            return
        # if i in ans:
        #     continue
        ans.append(i)
        solve()
        ans.pop()
solve()
