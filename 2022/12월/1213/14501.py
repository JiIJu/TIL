# 14501 퇴사
import sys
N = int(input())
data = []
for i in range(N):
    a,b= map(int,sys.stdin.readline().split())
    data.append([a,b])

i = 0
maxv = 0
temp = [0]*(N+1)
for i in range(N-1,-1,-1):
    a,b = data[i]
    if a+i<=N:
        temp[i] = max(temp[i+1],b+temp[i+a])
    else:
        temp[i] = temp[i+1]

print(temp)



