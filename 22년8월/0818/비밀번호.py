for tc in range(1,11):
    N , data = input().split()
    stack = []
    for i in data:
        if len(stack)==0:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    print(f"#{tc} {''.join(stack)}")