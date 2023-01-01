# 1124 언더프라임

num = [1]*100001
num[0],num[1] = 0,0
prime = []
for i in range(2,100001):
    for j in range(2,100001//i+1):
        if i*j<100001:
            num[i*j]=0
for i in range(2,100001):
    if num[i]:
        prime.append(i)


A,B = map(int,input().split())
ans = [0]*(B+1)
cnt=0
for i in range(A,B+1):
    a=i
    for j in prime:
        if j>i//2:
            break
        while a%j==0:
            a = a//j
            ans[i]+=1
    if ans[i] in prime:
        cnt+=1
# cnt = 0
# for i in ans:
#     if num[i]:
#         cnt+=1
print(cnt)

