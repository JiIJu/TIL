# 숫자카드
import sys
N = int(input())

data = set(map(int,sys.stdin.readline().split()))
M = int(input())
card = list(map(int,sys.stdin.readline().split()))

for i in card:
    if i in data:
        print(1,end=' ')
    else:
        print(0,end=' ')