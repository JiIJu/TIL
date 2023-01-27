# 2346 풍선터뜨리기

N = int(input())
data = list(map(int,input().split()))
start = 0
index = [x for x in range(1,N+1)]
answer = []
temp = data.pop(0)
answer.append(index.pop(start))
while data:
    if temp<0:
        start = (start+temp)%len(data)
    else:
        start = (start+temp-1)%len(data)
    temp = data.pop(start)
    answer.append(index.pop(start))
for i in answer:
    print(i,end=' ')