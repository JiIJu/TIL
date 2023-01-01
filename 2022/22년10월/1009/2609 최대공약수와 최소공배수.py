def max_n(a,b):
    if a%b==0:
        return b
    else:
        return max_n(b,a%b)

def min_n(a,b):
    s = max_n(a,b)
    return a*b//s
n,m = map(int,input().split())
if m>n:
    n,m = m,n
print(max_n(n,m))
print(min_n(n,m))