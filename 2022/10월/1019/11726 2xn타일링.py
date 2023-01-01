n = int(input())

data = [0]*(1001)
data[1]=1
data[2]=2
data[3]=3
for i in range(4,1001):
    data[i] = data[i-2]+data[i-1]
print(data[n]%10007)