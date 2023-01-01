# 1138 한줄로 서기
import sys
N = int(input())

data = list(map(int,sys.stdin.readline().split()))
ans = [0]*(N)

for i in range(N):
    a = data[i]
    cnt = 0
    for j in range(N):
        if ans[j]==0 and cnt==a:
            ans[j] = i+1
            print(ans)
            break

        elif ans[j] == 0:
            cnt+=1
print(ans)