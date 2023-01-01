# 1449 수리공항승

N , L = map(int,input().split())
data = list(map(int,input().split()))
data.sort()

gap = [0]*N
for i in range(N-1):
    gap[i] = data[i+1]-data[i]

cnt = 1
tape = L
for i in gap:
    if i<tape:
        tape-=i
    else:
        tape = L
        cnt+=1
print(cnt)