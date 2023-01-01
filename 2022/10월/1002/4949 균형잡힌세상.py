


while True:
    stack = []
    data = list(input())
    if data[0] == '.' and len(data)==1:
        break

    n = len(data)

    for i in range(n):
        # print(stack)
        if data[i]=='(' or data[i]=='[':
            stack.append(data[i])
        elif data[i]==')':
            if len(stack)>0 and stack[-1]=='(':
                stack.pop()
            else:
                print('no')
                break
        if data[i]==']':
            if len(stack)>0 and stack[-1]=='[':
                stack.pop()
            else:
                print('no')
                break
        if data[i]=='.' and len(stack)==0:
            print('yes')

        elif data[i]=='.' and len(stack)>0:
            print('no')

