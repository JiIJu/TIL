# 16401 과자 나눠주기

# m명의 조카 N개의 과자
M , N = map(int,input().split())

data = list(map(int,input().split()))

start = 1
end = max(data)
data.sort()
while start<=end:
    mid = (start+end)//2
    cnt = 0
    for i in range(N):
        cnt += data[i]//mid
    if cnt>=M:
        start = mid+1
    else:
        end = mid-1
print(end)