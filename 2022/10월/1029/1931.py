import sys

N = int(input())
data = []
cnt = 0
for i in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))

data = sorted(data,key=lambda x:x[0])
data = sorted(data,key=lambda x:x[1])
# print(data)
maxv = 0
ans = [data[0]]

for i in range(1,len(data)):
    if ans[-1][1] <= data[i][0]:
        ans.append(data[i])
print(len(ans))
