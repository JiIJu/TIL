# 2407 조합

n , m = map(int,input().split())

ans = 1

def fact(n):
    if n<2:
        return 1
    else:
        return fact(n-1)*n
print(fact(n)//fact(n-m)//fact(m))