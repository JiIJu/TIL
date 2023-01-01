# 별찍기-10

N , B = map(int,input().split())

A = [list(map(int,input().split())) for _ in range(N)]
A2 = A




def mul(a,b):
    data = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                data[i][j] += a[i][k]*b[k][j]%1000
    return data

def divide(a,b):
    if b ==1:
        return a
    x = divide(a,b//2)
    if b%2:
        return mul(mul(x,x),a)
    else:
        return mul(x,x)
res = divide(A,B)
for i in range(N):
    for j in range(N):
        res[i][j] = res[i][j]%1000
for i in res:
    print(*i)
