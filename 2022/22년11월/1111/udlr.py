# 이코테 상하좌우
'''
5
R R R U D D
'''

import sys
N = int(input())

data = [[0]*N for _ in range(N)]

step = list(sys.stdin.readline().split())


di = [-1,0,1,0]
dj = [0,1,0,-1]
a,b=0,0
for i in step:
    if i == 'U' and 0<=a+di[0]<N and 0<=b+dj[0]<N:
       a += di[0]
       b += dj[0]
    elif i =='R'and 0<=a+di[1]<N and 0<=b+dj[1]<N:
        a += di[1]
        b += dj[1]
    elif i == 'D'and 0<=a+di[2]<N and 0<=b+dj[2]<N:
        a += di[2]
        b += dj[2]
    elif i=='L'and 0<=a+di[3]<N and 0<=b+dj[3]<N:
        a += di[3]
        b += dj[3]
print(a+1,b+1)