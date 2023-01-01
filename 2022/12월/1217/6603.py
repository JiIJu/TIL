#6603 로또

def comb():
    for i in range(1<<n):
        res = []
        for j in range(n):
            if i & (1<<j):
                res.append(num[j])
        if len(res)==6:
            ans.append(res)
while True:
    data = list(map(int,input().split()))
    if data[0]==0:
        break
    n = data[0]
    num = data[1:]
    ans = []
    comb()
    ans.sort()
    for i in ans:
        print(*i)
    print()