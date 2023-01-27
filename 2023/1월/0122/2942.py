# 2942 퍼거슨과사과
def gcd(a,b):
    if b>a:
        a,b = b,a
    while b>0:
        a,b = b,a%b
    return a
R , G = map(int,input().split())

a = gcd(R,G)
ans = []
for i in range(1,a+1):
    if a%i==0:
        ans.append(i)

for i in ans:
    print(i,R//i,G//i)