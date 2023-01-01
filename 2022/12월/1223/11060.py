# 11060 점프

N = int(input())
data = list(map(int,input().split()))
ans = [N+1 for i in range(N)]
ans[0]=0
temp = 0
for i in range(N):
    for j in range(1,data[i]+1):
        if i+j<N:
            ans[i+j] = min(ans[i+j],ans[i]+1)
        # print(ans)
# if ans[-1]==99999:
#     print(-1)
# else:

if ans[-1]==N+1:
    print(-1)
else:
    print(ans[-1])
