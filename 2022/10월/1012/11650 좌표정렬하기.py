N = int(input())

data = []

for i in range(N):
    x,y = map(int,input().split())
    data.append((x,y))
data.sort()
for i in data:
    print(*i)


