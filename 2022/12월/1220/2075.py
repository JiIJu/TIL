# 2075 N번째 큰수

import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    arr += list(map(int,sys.stdin.readline().split()))
    arr = sorted(arr,reverse=True)[:n]
print(arr[-1])