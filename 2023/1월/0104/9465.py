# 9465 스티커
import sys


T = int(input())

for tc in range(T):
    N = int(input())
    data = [list(map(int,sys.stdin.readline().split())) for _ in range(2)]

    dp = [[0]*N for _ in range(2)]
    dp[0][0],dp[1][0] = data[0][0],data[1][0]
    dp[0][1],dp[1][1] = dp[1][0]+data[0][1],dp[0][0]+data[1][1]

    for j in range(2,N):
        dp[0][j] = max(dp[1][j-1],dp[1][j-2]) + data[0][j]
        dp[1][j] = max(dp[0][j - 1], dp[0][j - 2]) + data[1][j]
    print(max(dp[0][N-1],dp[1][N-1]))