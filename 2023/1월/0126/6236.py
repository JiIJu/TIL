# 6236 용돈관리
import sys
N , M = map(int,input().split())
data = []
for i in range(N):
    data.append(int(sys.stdin.readline()))
start=min(data)
end = sum(data)
ans = 0
while start<=end:
    mid = (start+end)//2
    charge = mid
    num= 1
    for i in range(N):
        if charge<data[i]:
            charge = mid
            num+=1
        charge -= data[i]
    if num>M or mid<max(data):
        start = mid+1
    else:
        end = mid-1
    # print(start,end)
print(start)


