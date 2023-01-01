N = int(input()) # 색종이 장수

data = [list(map(int,input().split())) for _ in range(N)]



a = [[0] * 1001 for _ in range(1001)]

for i in range(N):
    for j in range(data[i][0],data[i][0]+data[i][2]):
        for k in range(data[i][1],data[i][1]+data[i][3]):
            a[j][k] = i+1

cnt = [0]*(N+1)
for i in range(1,N+1):
    for j in a:
        cnt[i] += j.count(i)
    print(cnt[i])