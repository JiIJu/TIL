#1427 소트인사이드

N = list(input())
N.sort()
N = N[::-1]
for i in N:
    print(i,end='')

