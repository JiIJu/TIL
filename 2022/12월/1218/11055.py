# 11055 가장 큰 증가 부분 수열


N = int(input())
data = list(map(int,input().split()))
ans = [i for i in data]

for i in range(N):
    for j in range(i):
        if data[i]>data[j]:
            ans[i] = max(ans[i],ans[j]+data[i])
print(max(ans))