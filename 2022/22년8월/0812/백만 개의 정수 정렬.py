data = list(map(int,input().split()))
count= 0
for i in data:
    count +=1
for i in range(count):
    for j in range(count-i-1):
        if data[j] > data[j+1]:
            data[j] , data[j+1] = data[j+1] , data[j]
print(data[500000])

