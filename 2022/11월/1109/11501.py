# 11501 주식
import sys
T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(int,sys.stdin.readline().split()))
    ans = 0
    now = data[-1]
    for i in range(N-1,-1,-1):
        if data[i]>now:
            now = data[i]
        else:
            ans += now-data[i]
    print(ans)