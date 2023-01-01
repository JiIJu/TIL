import sys
N,K = map(int,input().split())

data1 = list(map(int,sys.stdin.readline().split()))
data2 = list(map(int,sys.stdin.readline().split()))

data1.sort()
data2 = sorted(data2)[::-1]

for i in range(K):
    if data1[i]<data2[i]:
        data1[i],data2[i] = data2[i],data1[i]
    else:
        break
print(data1)