# 1448 삼각형만들기
from itertools import combinations
import sys
N = int(input())
data = []
for i in range(N):
    data.append(int(sys.stdin.readline()))

data.sort()
data = data[::-1]
ans=-1
for i in range(N-2):
    if data[i]<data[i+1]+data[i+2]:
        ans = max(ans,data[i]+data[i+1]+data[i+2])
print(ans)