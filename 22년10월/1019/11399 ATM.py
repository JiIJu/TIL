import sys

N = int(input())

data = list(map(int,sys.stdin.readline().split()))

data.sort()
ans = [0]*N
ans[0]=data[0]
for i in range(1,N):
    ans[i]=ans[i-1]+data[i]
print(sum(ans))