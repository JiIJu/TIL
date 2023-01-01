T = int(input())

for tc in range(1,T+1):
    data = list(input())
    stack = []
    N =  len(data)
    top = 0
    ans = ''
    # stack.append(data[0])
    for i in range(N):
        if stack:
            if stack[-1] == data[i]:
                stack.pop()
            else:
                stack.append(data[i])
        else:
            stack.append(data[i])

    print(f'{tc} {len(stack)}')
