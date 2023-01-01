# 11660 구간합구하기 5
import sys
N , M = map(int,input().split())
data = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
new = [[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        new[i][j] = new[i][j-1]+new[i-1][j]-new[i-1][j-1]+data[i-1][j-1]
for i in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    print(new[x2][y2]-new[x1-1][y2]-new[x2][y1-1]+new[x1-1][y1-1])