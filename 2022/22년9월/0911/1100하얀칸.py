data = []
count=0
for i in range(8):
    data.append(list(input()))
white = [[1]*8 for _ in range(8)]
for i in range(0,8,2):
    for j in range(0,8,2):
        white[i][j] = 0
for i in range(1,8,2):
    for j in range(1,8,2):
        white[i][j] = 0
for i in range(8):
    for j in range(8):
        if data[i][j]=='F' and white[i][j]==0:
            count +=1
print(count)