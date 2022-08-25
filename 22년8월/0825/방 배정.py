N , K = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]

student = [[0]*2 for _ in range(7)]


for i in range(N):
    if data[i][0] == 0:
        student[data[i][1]][0] +=1
    else:
        student[data[i][1]][1] +=1

room = 0

for i in range(1,7):
    for j in range(2):
        if 0<student[i][j]<=K:
            room +=1
            student[i][j]=0
        elif student[i][j]>K:
            while student[i][j]:
                if student[i][j]-K>0:
                    room+=1
                    student[i][j] = student[i][j]-K
                else:
                    room +=1
                    student[i][j] = 0

print(room)