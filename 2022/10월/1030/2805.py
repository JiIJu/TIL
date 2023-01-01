import sys
N , M = map(int,input().split())

data = list(map(int,sys.stdin.readline().split()))
# data = sorted(data)[::-1]
s , e = 1 , max(data)
m = (s+e)//2
tree = 0

while s<=e:
    tree = 0
    m = (s+e)//2
    for i in data:
        if i - m>=0:
            tree = tree + i - m
            # print(tree)
    if M>tree:
        e = m-1
    elif M<=tree:
        s = m+1


print(e)