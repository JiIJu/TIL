
data = [list(map(int,input().split())) for _ in range(4)]

x1 , x2 = [] , []

for i in range(4):
    if data[i][0]>data[i][2]:
        data[i][0],data[i][2] = data[i][2],data[i][0]
    if data[i][1]>data[i][3]:
        data[i][1],data[i][3] = data[i][3] , data[i][1]
    x1 += [[data[i][0],data[i][1]]]
    x2 += [[data[i][2],data[i][3]]]

count = 0
s = [[0] * (101) for _ in range(101)]

for i in range(4):
    for j in range(x1[i][0],x2[i][0]):
        for k in range(x1[i][1],x2[i][1]):
            s[k][j] = 1
for i in range(101):
    for j in range(101):
        if s[i][j] ==1:
            count+=1
print(count)