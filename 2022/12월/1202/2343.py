# 2343 기타레슨

N , M = map(int,input().split())
data = list(map(int,input().split()))
end = sum(data)
start = max(data)

while start<=end:
    mid =(start+end)//2
    cnt = 0
    tmp = 0
    for i in range(N):
        if tmp+data[i] > mid:
            cnt +=1
            tmp = 0
        tmp += data[i]
    if tmp:
        cnt+=1
    else:
        pass
    if cnt<=M:
        end = mid-1
    else:
        start = mid+1

print(start)
