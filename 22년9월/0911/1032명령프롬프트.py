N = int(input())
data = []
for i in range(N):
    a = list(input())
    data.append(a)
# print(data)
n = len(data[0])
new = []

for i in range(n):
    check = []
    result = -1
    for j in range(N):
        check.append(data[j][i])
    for j in range(N-1):
        if check[j]!=check[j+1]:
            result = 0
    if result == 0:
        new.append('?')
    else:
        new.append(check[0])

for i in range(n):
    print(new[i],end='')