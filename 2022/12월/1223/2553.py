# 2553 마지막 팩토리얼 수


N = int(input())
ans =1
for i in range(1,N+1):
    ans*=i
    while ans%10==0:
        ans = ans//10
    ans = ans%1000000
ans = str(ans)
for i in ans[::-1]:
    if i!='0':
        print(i)
        break