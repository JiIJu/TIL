# 11568 민균이의 계략

N = int(input())

data = list(map(int,input().split()))

num = [1]*1001

for i in range(N):
    for j in range(i):
        if data[i]>data[j]:
            num[i] = max(num[i],num[j]+1)
print(max(num))