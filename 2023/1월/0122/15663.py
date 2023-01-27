# 15663 N과M(9)


N,M = map(int,input().split())
data = list(map(int,input().split()))
ans = []
dic = {}
data.sort()
check = [0]*N
def solve(a):
    if a==M:
        s = ' '.join(map(str,ans))
        if s not in dic:
            dic[s]=1
            print(s)
        return
    for i in range(N):
        if check[i]==0:
            ans.append(data[i])
            check[i]=1
            solve(a+1)
            ans.pop()
            check[i]=0

solve(0)

