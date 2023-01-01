switch_num= int(input())

a = list(map(int,input().split()))
student_num = int(input())
student = [list(map(int,input().split())) for _ in range(student_num)]

switch = [-1]
for i in range(switch_num):
    switch += [a[i]]

n = 1
for i in range(student_num):
    if student[i][0] == 1:
        for j in range(1,switch_num+1):
            if j%student[i][1]==0:
                switch[j] = (switch[j]+1)%2

    else:
        switch[student[i][1]] = (switch[student[i][1]] + 1) % 2
        while True:

            if (student[i][1]+n)<(switch_num+1) and (student[i][1]-n)>=0 and switch[student[i][1]+n] == switch[student[i][1]-n]:
                switch[student[i][1]+n] = (switch[student[i][1]+n]+1)%2
                switch[student[i][1] - n] = (switch[student[i][1]-n]+1) %2
                n+=1

            else:
                n = 1
                break

for i in range(1,switch_num+1):
    print(switch[i],end=' ')
    if i%20==0:
        print()


# 1 1 1 1 1
# 0 0 0 0 0
# 1 1 1 0 0
# 1 1 0 0 0
# 1 1 1 1 1
# 1 1 1 1 0