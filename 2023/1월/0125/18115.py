# 18115  카드놓기
from collections import deque

N = int(input())
data = list(map(int,input().split()))
temp = [i for i in range(1,N+1)]

ans = deque()
si = 1
for i in range(N-1,-1,-1):
    if data[i]==1:
        ans.appendleft(si)
    elif data[i]==2:
        a = ans.popleft()
        ans.appendleft(si)
        ans.appendleft(a)
    else:
        ans.append(si)
    si+=1

## 1 2 3 4 5
# 1 2
print(*list(ans))