# 2312 수 복원하기

# def solve(a,b):
#     while b>1:
#         a,b = b,a%b
#     return a


num =[1]*100001
num[0],num[1] = 0,0
for i in range(2,100001):
    for j in range(2,100001//i+1):
        if i*j<100001:
            num[i*j]=0

T = int(input())
for tc in range(T):
    N = int(input())
    ans = [0]*(N+1)
    for i in range(2,N+1):
        if num[i]==1:
            a = N
            while a%i==0:
                a = a//i
                ans[i]+=1
    for i in range(len(ans)):
        if ans[i]:
            print(i,ans[i])
