# 1080 행렬


N,M = map(int,input().split())

data_A = [list(input()) for _ in range(N)]
data_B = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        data_A[i][j],data_B[i][j] = int(data_A[i][j]),int(data_B[i][j])


def reverse(x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            data_A[i][j] = 1-data_A[i][j]
cnt=0
for i in range(N-2):
    for j in range(M-2):
        if data_A[i][j]!=data_B[i][j]:
            reverse(i,j)
            cnt+=1
        if data_A==data_B:
            break
    if data_A==data_B:
        break
if data_A==data_B:
    print(cnt)
else:
    print(-1)