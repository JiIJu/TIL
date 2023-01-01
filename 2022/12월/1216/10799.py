# 10799 쇠막대기

pipe = input()
cnt=0
N = len(pipe)
i = 0
stack = []

while i<N:
    if pipe[i]=='(':
        stack.append(pipe[i])
    elif pipe[i-1]=='(' and pipe[i]==')':
        stack.pop()
        cnt+=len(stack)
    elif pipe[i]==')':
        stack.pop()
        cnt+=1

    i+=1
print(cnt)

