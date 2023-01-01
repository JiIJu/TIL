#11279 최대힙

import sys
import heapq
N = int(sys.stdin.readline())

data = []

for i in range(N):
    a = int(sys.stdin.readline())

    if a>0:
        heapq.heappush(data,a)
    else:
        if data:
            print(heapq.heappop(data))

        else:
            print(0)