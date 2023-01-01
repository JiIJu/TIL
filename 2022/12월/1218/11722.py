# 11722 가장 긴 감소하는 부분 수열

N = int(input())
data = list(map(int,input().split()))
ans = [1]*N

for i in range(N):
    for j in range(i):
        if data[i]<data[j]:
            ans[i] = max(ans[i],ans[j]+1)

print(max(ans))