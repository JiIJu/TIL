# 1946 신입사원
import sys
T = int(input())

for tc in range(T):
    N = int(input())
    num1 = [0]*(N+1)
    num2 = [0]*(N+1)
    num = []
    for i in range(N):
        a,b = map(int,sys.stdin.readline().split())
        num.append([a,b])
    num.sort(key=lambda x:x[0])

    cnt = 1
    temp = num[0][1]
    for i in  range(1,N):
        if temp>num[i][1]:
            cnt+=1
            temp = num[i][1]
    print(cnt)