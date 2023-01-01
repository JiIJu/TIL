# 10773 제로
import sys
K = int(input())
data = []
cnt=0
res = []
for i in range(K):
    n = int(sys.stdin.readline())
    if n ==0:
        data.pop(-1)
    else:
        data.append(n)
print(sum(data))