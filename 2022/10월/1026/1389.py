# 1389 케빈베이컨의 6단계 법칙
import sys
from collections import deque


def bfs(s):
    num = [0]*(N+1)
    visit[s]=1
    q = [s]

    while q:
        a = q.pop(0)
        for i in data[a]:
            if visit[i]==0:
                visit[i]=1
                q.append(i)
                num[i] = num[a]+1
    return sum(num)










# def bfs(data,s):
#     num = [0]*(N+1)
#     q = []
#     visit[s] = 1
#     q.append(s)
#     while q:
#         a = q.pop(0)
#         for i in data[a]:
#             if visit[i] == 0:
#                 num[i] = num[a]+1
#                 q.append(i)
#                 visit[i] = 1
#                 print(num)
#     return sum(num)
N,M = map(int,input().split())

data = [[] for _ in range(N+1)]

for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    data[a].append(b)
    data[b].append(a)



ans = []
for i in range(1,N+1):
    visit = [0] * (N + 1)
    z = bfs(i)
    ans.append(z)

print(ans.index(min(ans))+1)