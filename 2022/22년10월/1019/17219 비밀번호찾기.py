import sys

N , M = map(int,sys.stdin.readline().split())
data1 = []
data2 = []
for _ in range(N):
    a,b = sys.stdin.readline().split()
    data1.append(a)
    data2.append(b)
ans = []
for _ in range(M):
    temp = sys.stdin.readline().strip()
    a = data1.index(str(temp))
    print(data2[a])