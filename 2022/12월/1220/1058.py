# 1058 친구

N = int(input())
data = [list(input()) for _ in range(N)]
friend = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if i==k:
                continue
            if data[i][k]=='Y' or (data[i][j]=='Y' and data[j][k]=='Y'):
                friend[i][k] = 1
maxv= 0
for i in friend:
    maxv = max(sum(i),maxv)
print(maxv)

