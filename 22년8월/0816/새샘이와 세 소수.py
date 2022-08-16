# 에라토스테네스의 체

def era(n):

    a = [True] * (n + 1)
    m = int(n**0.5)
    b = []
    for i in range(2, m + 1):
        if a[i] == True:
            for j in range(i + i, n + 1, i):
                a[j] = False

    for i in range(2, n + 1):
        if a[i] == True:
            b += [i]
    return b


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    num = era(N)
    a = len(num)
    count=0
    data =[]
    emp = []
    for i in range(a):
        for j in range(a):
            for k in range(a):
                if num[i]+num[j]+num[k]==N:
                    count +=1
                    data += [i,j,k]
    v = ''
    for i in range(len(data)):
        emp[i] += data[i:i+2]
    print(data)
    print(count)
    print(emp)
    # print(f'#{tc} {count}')