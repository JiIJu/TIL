T = int(input())

for tc in range(1,T+1):
    stack = []
    a = []
    data = input()
    data_len = len(data)
    result = 1
    for i in data:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack)==0:
                result = 0
                break
            elif stack[-1] != '(':
                result = 0
                break
            stack.pop()
        elif i == '{':
            stack.append(i)
        elif i == '}':
            if len(stack)==0:
                result = 0
                break
            elif stack[-1] != '{':
                result = 0
                break
            stack.pop()
    if len(stack) != 0:
        result = 0
    print(f'#{tc} {result}')

