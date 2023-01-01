# 수들의합

N , M = map(int,input().split())
data = list(map(int,input().split()))
cnt = 0
for i in range(N):
    sumv = 0
    for j in range(i,N):
        sumv+=data[j]
        if sumv>M:
            break
        elif sumv==M:
            cnt+=1
            break
print(cnt)