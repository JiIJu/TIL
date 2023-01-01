# 2477 참외밭

N = int(input())
data = []
direct = []
for i in range(6):
    a,b = map(int,input().split())
    direct.append(a)
    data.append(b)

max_length , min_length = [],[]
for i in range(6):
    if direct.count(direct[i]) ==1:
        max_length.append(data[i])
        temp = i+3
        if temp>=6:
            temp-=6
        min_length.append(data[temp])
print((max_length[0]*max_length[1]-min_length[0]*min_length[1])*N)