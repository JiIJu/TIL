# 2193 이친수

N = int(input())

data = [0] * 91
data[1] = 1
data[2] = 1
data[3] = 2
data[4] = 3
for i in range(5,91):
    data[i] = data[i-1]+data[i-2]
print(data[N])