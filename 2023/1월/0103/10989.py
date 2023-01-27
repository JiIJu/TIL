# 10989 수 정렬하기3
import sys
N = int(input())
data = {}

for i in range(N):
    n = int(sys.stdin.readline())
    if n in data:
        data[n] +=1
    else:
        data[n]=1

for i in range(1,10001):
    if i in data:
        for j in range(data[i]):
            print(i)