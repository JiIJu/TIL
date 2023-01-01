n = int(input())

data =[0]*100001

data[1],data[2],data[3],data[4],data[5]=-1,1,-1,2,1

for i in range(6,100001):
    if data[i-5]>=1:
        data[i] = data[i-5] +1
    elif data[i-2] >=1:
        data[i] = data[i-2]+1
    else:
        data[i] = -1
print(data[n])