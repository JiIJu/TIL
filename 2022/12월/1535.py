# 1535 안녕

N = int(input())

L = list(map(int,input().split()))
J = list(map(int,input().split()))

data = [[0]*101 for _ in range(N+1)]

for i in range(1,N+1):
    s = L[i-1]
    p = J[i-1]

    for j in range(1,101):
        if j<=s:
            data[i][j] = data[i-1][j]
        else:
            data[i][j] = max(data[i-1][j],p+data[i-1][j-s])

print(data)