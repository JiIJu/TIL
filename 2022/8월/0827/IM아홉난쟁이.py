data = [int(input()) for _ in range(9)]

sum = 0
total = 0
ans = 0
a= []
for i in range(9):
    total += data[i]

for i in range(8):
    for j in range(i+1,9):
        if total-(data[i]+data[j])==100:
            a += [i,j]

result = []
for i in range(9):
    if i != a[0] and i != a[1]:
        result.append(data[i])
result.sort()
for i in result:
    print(i)
