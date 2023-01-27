# 17829 222-풀링
import sys

def solve(x,y,N):
    mid = N//2
    if N==2:
        answer = [data[x][y],data[x+1][y],data[x][y+1],data[x+1][y+1]]
        answer.sort()
        return answer[-2]
    answer = [solve(x,y,mid),solve(x+mid,y,mid),solve(x,y+mid,mid),solve(x+mid,y+mid,mid)]
    answer.sort()
    return answer[-2]
N = int(input())

data = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
print(solve(0,0,N))