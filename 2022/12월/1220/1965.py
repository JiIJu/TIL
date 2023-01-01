# 1965 상자넣기

N = int(input())
data = list(map(int,input().split()))
ans = [1]*(N)

for i in range(N-1):
    for j in range(i+1,N):
        if data[i]<data[j]:
            ans[j] = max(ans[j],ans[i]+1)
print(max(ans))