# 1446 지름길

N,D = map(int,input().split())
data = []

for i in range(N):
    start , end , distance = map(int,input().split())
    data.append((start,end,distance))
data.sort()

ans = 0
num = [i for i in range(10001)]
for j in range(D+1):
    num[j] = min(num[j],num[j-1]+1)
    for start,end,distance in data:
        if num[end]>num[start]+distance:
            num[end] = num[start]+distance
            for i in range(end+1,10001):
                num[i] = num[i-1]+1

print(num[D])