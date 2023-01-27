# 1850 최대공약수

def gcd(a,b):
    if b>a:
        a,b = b,a
    while b>0:
        a,b = b,a%b
    return a


a,b = map(int,input().split())


print('1'*gcd(a,b))