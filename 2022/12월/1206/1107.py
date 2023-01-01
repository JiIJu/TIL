#리모콘
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
if M:
    a = list(map(int,input().split()))
else:
    a = []
minV = abs(100-N)
for i in range(1000001):
    num = str(i)

    for j in range(len(num)):
        if int(num[j]) in a:
            break
        elif j==len(num)-1:
            minV = min(minV,abs(i-N)+len(num))
print(minV)