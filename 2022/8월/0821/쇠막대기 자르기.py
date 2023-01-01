# T = int(input())
#
# for tc in range(1,T+1):
#     data = input()
#     stack = []
#     count = 0
#     for i in range(len(data)):
#         if data[i] == '(':
#             stack.append(data[i])
#         elif data[i] == ')':
#             if data[i-1] == '(':
#                 stack.pop()
#                 count+=len(stack)
#             elif data[i-1] == ')':
#                 count+=1
#                 stack.pop()
#     print(f'#{tc} {count}')




T = int(input())

for tc in range(1,T+1):
    data = input()
    stack = []
    count = 0
    for i in range(len(data)):
        if data[i] == '(':
            stack.append(data[i])
        elif data[i] == ')':
            if data[i-1] == '(':
                stack.pop()
                count+=len(stack)
            elif data[i-1] == ')':
                stack.pop()
                count+=1
    print(f'#{tc} {count}')







