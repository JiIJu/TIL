paper =[[0]*100 for _ in range(100)]

N = int(input())

data = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(data[i][0],data[i][0]+10):
        for k in range(data[i][1],data[i][1]+10):
            paper[j][k] = 1
cnt = 0
for i in range(100):
    for j in range(100):
        if paper[i][j]==1:
            cnt+=1
print(cnt)