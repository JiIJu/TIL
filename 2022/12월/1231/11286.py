# 11286 절댓값 힙
import sys
import heapq
N = int(input())
data = []
for i in range(N):
    x = int(sys.stdin.readline())
    if x!=0:
        heapq.heappush(data,(abs(x),x))
    else:
        if data:
            print(heapq.heappop(data)[1])
        else:
            print(0)