N = int(input()) #학생수
data = list(map(int,input().split())) # 학생들이 뽑은 번호
student = [0] * (N)
stack=[]
for i in range(N):
    student[i] = i+1


a = []
stack.append(student[0])
for i in range(1,N):
    if data[i] == 0:
        stack.append(student[i])
    else:
        for j in range(data[i]):
            a.append(stack.pop())
        stack.append(student[i])

        for j in range(data[i]):
            stack.append(a.pop())


print(*stack)

