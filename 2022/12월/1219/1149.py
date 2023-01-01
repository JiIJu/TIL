# 1149 RGB거리
import sys

N = int(input())

data = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

check = [[0]*3 for _ in range(N)]
for i in range(3):
    check[0][i] = data[0][i]
for i in range(1,N):
    check[i][0] = min(check[i-1][1],check[i-1][2])+data[i][0]
    check[i][1] = min(check[i - 1][2], check[i - 1][0]) + data[i][1]
    check[i][2] = min(check[i - 1][0], check[i - 1][1]) + data[i][2]

print(min(check[N-1]))