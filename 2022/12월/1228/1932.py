# 정수삼각형 1932

N = int(input())
data = []
for i in range(N):
    data.append(list(map(int,input().split())))

temp = 2

for i in range(1,N):
    for j in range(temp):
        if j==0:
            data[i][j] = data[i][j]+data[i-1][j]
        elif j==i:
            data[i][j] = data[i-1][j-1]+data[i][j]
        else:
            data[i][j] = max(data[i-1][j-1]+data[i][j],data[i][j]+data[i-1][j])
    temp+=1
print(data)