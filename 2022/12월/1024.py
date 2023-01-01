# 1024 수열의합

N,L = map(int,input().split())

res = 1
for i in range(L,101):
    temp = N//i
    ans = []
    if i%2:
        for j in range(i//2,-1,-1):
            if temp-j>=0:
                ans.append(temp-j)
        for j in range(1,i//2+1):
            ans.append(temp+j)
    else:
        for j in range(i//2-1,-1,-1):
            if temp - j >= 0:
                ans.append(temp-j)
        for j in range(1,i//2+1):
            ans.append(temp+j)
    if sum(ans)==N and len(ans)>=L:
        res = 0
        break
# if N==1:
    # print(0,1)
if res==1:
    print(-1)
else:
    print(*ans)

