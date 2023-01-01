# 한수

N = int(input())

data = [0] * 1001
for i in range(1,100):
    data[i] = i
for i in range(100,N+1):
    a = str(i)
    tmp = 0
    for j in range(len(a)-2):
        q = int(a[j])
        w = int(a[j+1])
        e = int(a[j+2])
        if w-q == e-w:
            pass
        else:
            tmp=1
            break
    if tmp==0:
        data[i] = data[i-1]+1
    else:
        data[i] = data[i-1]
print(data[N])