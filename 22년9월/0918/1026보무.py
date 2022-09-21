N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

data = [0]*N

a = sorted(B)
a = a[::-1]

A.sort()

sum = 0
for i in range(N):
    sum += A[i]*a[i]
print(sum)