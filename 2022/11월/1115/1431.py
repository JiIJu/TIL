# 1431 시리얼 번호

N = int(input())

data = []
for i in range(N):
    data.append(input())


def sum_num(x):
    res = 0
    for i in x:
        if '0'<=i<='9':
            res+=int(i)
    return res

data.sort(key = lambda x:(len(x),sum_num(x),x))
for i in data:
    print(i)