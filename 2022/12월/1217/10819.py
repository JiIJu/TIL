# 10819 차이를 최대로

N = int(input())

data = list(map(int,input().split()))
ans = []
visit = [0]*N
maxv = -99999
def solve():
    global maxv
    for i in range(N):
        if len(ans)==N:
            temp=0
            for i in range(N-1):
                temp+=abs(ans[i]-ans[i+1])
            maxv = max(maxv,temp)
            return
        if visit[i]==1:
            continue
        ans.append(data[i])
        visit[i]=1
        solve()
        visit[i]=0
        ans.pop()
solve()
print(maxv)

'''
ans = []
def solve()
    for i in range(N):
        if len(ans)==k:
            print(ans)
        if i in ans:
            continue
        ans.append(i)
        solve()
        ans.pop()    
'''