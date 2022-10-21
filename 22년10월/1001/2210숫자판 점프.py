def asd(i,j,n):
    if len(n)==6:
        if n not in check:
            check.append(n)
        return
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0<=ni<5 and 0<=nj<5:

            asd(ni,nj,n+data[ni][nj])


data = [list(input().split()) for _ in range(5)]
check = []
visit = [[0]*5 for _ in range(5)]
di = [-1,1,0,0]
dj = [0,0,-1,1]
for i in range(5):
    for j in range(5):
        asd(i,j,f'{data[i][j]}')

print(len(check))