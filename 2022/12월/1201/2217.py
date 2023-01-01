#2217 로프
import sys
N = int(input())
data = []
for i in range(N):
    data.append(int(sys.stdin.readline()))

lope = [0]*(N+1)
data.sort(reverse=True)
lope[1]=data[0]
for i in range(2,N+1):
    lope[i] = data[i-1]*i
print(max(lope))