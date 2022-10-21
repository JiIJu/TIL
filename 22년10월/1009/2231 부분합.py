N = int(input())
ans=[]
n = N
l = str(N)
length = len(l)
while n>N-10*length:    # 숫자 자기자신과 각 자리수의 합을 구하기때문에 모든 범위의 수를 찾을 필요가 없이
    a = n               # 몇자리수인지 파악후 그 자리수*10만큼만 탐방하면 시간초과를 피할수있음
    b = n
    while b>0:
        a+=b%10
        b = b//10
    if a == N:
        ans.append(n)
    n -=1
if ans:
    print(ans[-1])
else:
    print(0)