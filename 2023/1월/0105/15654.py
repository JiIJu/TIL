# 15654 N과M(5)

def dfs():
    if len(ans)==M:
        check=0
        for i in range(1,M):
            if ans[i]<ans[i-1]:
                check=1
                break
        if check==0:
            print(*ans)
        return
    for i in data:
        ans.append(i)
        dfs()
        ans.pop()
N,M = map(int,input().split())
data = list(map(int,input().split()))
data.sort()
ans = []
dfs()
