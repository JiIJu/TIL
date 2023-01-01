# 17087 숨바꼭질 6
def solve(a,b):
    if b>a:
        a,b=b,a
    while b>0:
        a,b = b,a%b
    return a

N , S = map(int,input().split())

data = list(map(int,input().split()))
temp = []
for i in data:
    temp.append(abs(i-S))
temp.sort()
maxv = 99999999
if len(temp)==1:
    maxv = temp[0]
else:
    maxv = solve(temp[0],temp[1])
    for i in range(1,len(temp)-1):
        maxv = min(solve(temp[i],temp[i+1]),maxv)

print(maxv)
