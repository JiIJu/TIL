import sys , heapq
N = int(input())


ans = []
for i in range(N):
    a = int(sys.stdin.readline())
    if a >0:
        heapq.heappush(ans,a)
    else:
        if len(ans):
            minv = heapq.heappop(ans)
            print(minv)
        else:
            print(0)
