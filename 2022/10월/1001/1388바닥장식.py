N,M = map(int,input().split())

data = [list(input()) for _ in range(N)]

cnt = 0

for i in range(N):
    a = ''
    for j in range(M):
        if data[i][j] == '-' and data[i][j]!=a:
            cnt+=1
        a= data[i][j]

for i in range(M):
    a=''
    for j in range(N):
        if data[j][i]=='|' and data[j][i]!=a:
            cnt+=1
        a=data[j][i]
print(cnt)