# 1500 쵀대곱

S,K = map(int,input().split())

a = S//K
b = S%K
n=1

while K>0:
    if b>0:
        n = n*(a+1)
        b-=1
    else:
        n = n*a
    K-=1
print(n)