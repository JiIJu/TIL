T = int(input())

for tc in range(1,T+1):
    data = list(input().split())
    n = len(data)
    stack = []
    icp = {'+':1,'-':1,'*':2,'/':2}
    postfix = []
    result = 0
    count = 0
    cnt = 0
    for i in range(n):
        if '0'<=data[i]<='9':
            count+=1
        else:
            cnt+=1

    for i in range(n-1):
        if '0'<=data[i]<='9':
            stack.append(data[i])
        elif len(stack)>=2 and (data[i]=='+' or data[i] == '-' or data[i] == '/' or data[i] == '*'):
            a = int(stack.pop())
            b = int(stack.pop())
            if data[i] == '+':
                result = a+b
            elif data[i] == '-':
                result = b-a
            elif data[i] == '*':
                result = b*a
            elif data[i] == '/':
                result = b//a
            stack.append(result)
    if count==cnt:
        print(f'#{tc} {stack[-1]}')
    else:
        print(f'#{tc} error')



