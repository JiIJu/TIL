# 2839 설탕배달

N = int(input())

data = [0]*5001
data[1] = -1
data[2]=-1
data[3]=1
data[4]=-1
data[5]=1
for i in range(6,5001):
    temp=0
    if data[i-3]!=-1:
        data[i] = data[i-3]+1
        temp=1
    if data[i-5]!=-1:
        data[i] = data[i-5]+1
        temp=1
    if temp==0:
        data[i]=-1
print(data[N])
