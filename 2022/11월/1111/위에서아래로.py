N = int(input())

data = []
for i in range(N):
    data.append(int(input()))

data.sort()

print(*data[::-1])