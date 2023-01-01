#2512 예산
import sys
N = int(input())

data = list(map(int,sys.stdin.readline().split()))
data.sort()
total = int(input())
ans = 0
mid = max(data)
cnt = 0
ANS =0
while True:
    ans = 0
    for i in data:
        if i <= mid:
            ans += i
        else:
            ans += mid
    if ANS == ans:
        break
    if ans>total:
        maxv = mid
        mid = (mid-1+maxv)//2

        ANS = ans
    else:
        minv= mid
        mid = (mid+1+minv)//2
        ANS = ans
    cnt+=1

print(mid)