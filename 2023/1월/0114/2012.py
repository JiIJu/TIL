# 2012 등수 매기기

N = int(input())
num = []
for i in range(N):
    num.append(int(input()))
num.sort()
ans = 0
for i in range(1,N+1):
    ans += abs(i-num[i-1])
print(ans)
