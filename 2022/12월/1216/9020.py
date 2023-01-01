# 9020 골드바흐의 추측

num = [0] * 10001
num[1] = -1
for i in range(2,10001):
    for j in range(2,int(10001//i)):
        if i*j<10001:
            num[i*j] = -1

prime = []
for i in range(2,10001):
    if num[i]==0:
        prime.append(i)

N = int(input())
for i in range(N):
    data = int(input())
    a,b = data//2 , data//2
    while a>0:
        if a in prime and b in prime:
            print(a,b)
            break
        else:
            a-=1
            b+=1
