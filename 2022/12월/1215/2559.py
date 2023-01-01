# 2559 수열

N , K = map(int,input().split())
data = list(map(int,input().split()))
pre_sum = [0]*(N+1)
pre_sum[1] = data[0]
for i in range(2,N+1):
    pre_sum[i] = pre_sum[i-1] + data[i-1]
maxv = -9999999
end = 0
for i in range(N-K,-1,-1):
    maxv = max(maxv,pre_sum[i+K]-pre_sum[i])
print(maxv)