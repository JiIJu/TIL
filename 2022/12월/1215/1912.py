# 1912 연속합

n = int(input())
data = list(map(int,input().split()))
ans = [data[0]]
for i in range(n-1):
    ans.append(max(ans[i]+data[i+1],data[i+1]))
print(max(ans))