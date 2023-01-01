# 2961 도영이가 만든 맛있는 음

def comb():
    for i in range(1,1<<N):
        res = []
        for j in range(N):
            if i&(1<<j):
                res.append(data[j])
        # if res:
        com.append(res)

N = int(input())
data = []
for i in range(N):
    S , B = map(int,input().split())
    data.append([S,B])
com = []
comb()
minv = 999999999
for i in com:
    a = 1
    b = 0
    for j in i:
        a*=j[0]
        b+=j[1]
    minv = min(minv,abs(a-b))
print(minv)
