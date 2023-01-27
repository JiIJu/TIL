# 2548 대표자연수

N = int(input())
data= list(map(int,input().split()))
num = [0]*(20001)
temp = sum(data)

num[0]=10**9
for i in range(1,len(num)):
    for j in range(N):
        num[i] += abs(i-data[j])
minv = min(num)

for i in range(1,len(num)):
    if num[i]==minv:
        print(i)
        break