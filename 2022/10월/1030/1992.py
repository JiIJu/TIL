import sys

N = int(input())

data = [list((sys.stdin.readline().strip('\n'))) for _ in range(N)]

for i in range(N):
    for j in range(N):
        data[i][j] = int(data[i][j])

# 몇사분면인지 파악
w