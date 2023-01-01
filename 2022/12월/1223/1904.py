# 01타일 1904

ans = [0]*1000001
ans[1],ans[2],ans[3],ans[4]=1,2,3,5
N = int(input())
for i in range(5,N+1):
    ans[i] = (ans[i-2]+ans[i-1])%15746
print(ans[N])