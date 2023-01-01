# 별찍기 - 10
def star(N):
    if N==3:
        return ['***','* *','***']

    arr = star(N//3)
    res = []
    for i in arr:
        res.append(i*3)

    for i in arr:
        res.append(i+' '*(N//3)+i)
    for i in arr:
        res.append(i*3)
    return res

N = int(input())
data = star(N)
for i in data:
    print(i)