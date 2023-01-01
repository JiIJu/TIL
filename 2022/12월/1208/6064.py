# 카잉달

def gcd(a,b):
    while b>0:
        a,b = b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)
T = int(input())

for tc in range(T):
    M , N , x , y = map(int,input().split())
    cnt=0

    maxv = lcm(M,N)
    cnt=0
    a,b = 1,1
    tmp=0
    while a<=maxv and b<=maxv:
        a = M*cnt + x

        if (a - y)%N==0:
            tmp=1
            break
        cnt+=1
    if tmp==1:
        print(a)
    else:
        print(-1)
'''
15
40000 39999 39999 39998
40000 39999 40000 39999
40000 40000 40000 39999
40000 39998 40000 39997
39999 2 39998 2
3 40000 3 39999
40000 3 40000 3
8 2 4 2
10 12 2 12
12 10 12 10
12 10 1 1
12 6 12 6
10 1 5 1
1 10 1 5
1 1 1 1'''