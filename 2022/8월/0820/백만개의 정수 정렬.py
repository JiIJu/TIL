data = list(map(int,input().split()))

num = [0] * 1000001
arr = [0] * 1000000
for i in range(1000000):
    num[data[i]] +=1
for i in range(1,1000001):
    num[i] += num[i-1]
for i in range(999999,-1,-1):
    num[data[i]] -= 1
    arr[num[data[i]]] = data[i]
print(arr[500000])