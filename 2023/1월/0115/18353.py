# 18353 병사 배치하기

N = int(input())
data = list(map(int,input().split()))

data = data[::-1]

num = [1]*N

for i in range(N):
    for j in range(i):
        if data[j]<data[i]:
            num[i] = max(num[i],num[j]+1)
print(N-max(num))