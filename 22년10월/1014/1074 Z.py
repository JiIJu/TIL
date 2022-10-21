
N , r, c = map(int,input().split())

m = 2**N
s=[]
a = 0
while m>1:
    m = m//2
    if r<m and c<m:
        s.append(1)
        d=0
    elif r<m and c>=m:
        s.append(2)
        c-=m
    elif r>=m and c<m:
        s.append(3)
        r-=m
    elif r>=m and c>=m:
        s.append(4)
        c-=m
        r-=m

ans = 4**N

for i in s:
    ans = ans//4
    a += (i-1)*ans

print(a)