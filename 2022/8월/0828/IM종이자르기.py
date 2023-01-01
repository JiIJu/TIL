n,m = map(int,input().split())
cut = int(input())
data = [list(map(int,input().split())) for _ in range(cut)]

paper = [[0]*n for _ in range(m)]


row = [0]
col = [0]
for i in range(cut):
    if data[i][0] == 0:
        row.append(data[i][1])
    elif data[i][0] == 1:
        col.append(data[i][1])
row.append(m)
col.append(n)
row.sort()
col.sort()
rmax = 0
cmax = 0

for i in range(len(row)-1):
    if row[i+1]-row[i]>rmax:
        rmax = row[i+1]-row[i]

for i in range(len(col)-1):
    if col[i+1]-col[i]>cmax:
        cmax = col[i+1]-col[i]
print(rmax*cmax)
