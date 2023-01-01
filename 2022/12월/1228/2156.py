# 2156 포도주 시식
import sys
N = int(input())
data = [0]*(N+1)

for i in range(N):
    data[i] = int(sys.stdin.readline())


num = [[data[0],0,0] for _ in range(N+1)]

for i in range(1,N):
    num[i][0] = max(num[i][0],num[i-1][2] + data[i])
    num[i][1] = max(num[i][1],num[i-1][0] + data[i])
    num[i][2] = max(num[i-1][0],num[i-1][1],num[i-1][2])
print(max(num[N-1]))
