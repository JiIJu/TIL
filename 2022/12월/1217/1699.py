# 1699 제곱수의 합

N = int(input())

num = [i for i in range(N+1)]

for i in range(1,N+1):
    for j in range(1,i):
        if j*j>i:
            break
        if num[i]>num[i-j*j]+1:
            num[i] = num[i-j*j]+1
print(num[N])