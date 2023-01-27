# 1629 곱셈

def mul(C,n):
    if n ==1:
        return C%D
    else:
        y = mul(C,n//2)
        if n%2==0:
            return (y*y)%D
        else:
            return (y*y*C)%D

A,B,D = map(int,input().split())
print(mul(A,B))