# icp = {'+':1,'-':1,'*':2,'/':2,'(':3}
# isp = {'+':1,'-':1,'*':2,'/':2,'(':0}
#
# for tc in range(1,11):
#     N = int(input())
#     data = input()
#     stack = []
#     text = ''
#
#     for i in range(N):
#         if '0'<=data[i]<='9':
#             text += data[i]
#         else:
#             if data[i] == ')':
#                 while True:
#                     if stack[-1] == '(':
#                         stack.pop()
#                         break
#                     text += stack.pop()
#             else:
#                 if len(stack)>0 and icp[data[i]]<=isp[stack[-1]] :
#                     text+=stack.pop()
#                 stack.append(data[i])
#     while stack:
#             text += stack.pop()
#
#     stack = []
#     n = len(text)
#
#     for i in range(n):
#         if '0'<=text[i]<='9':
#             stack.append(int(text[i]))
#         else:
#             a =0
#             b=0
#             c=0
#             a = stack.pop()
#             b = stack.pop()
#             if text[i] == '+':
#                 c = b+a
#             elif text[i] == '-':
#                 c = b-a
#             elif text[i] =='*':
#                 c = b*a
#             elif text[i] == '/':
#                 c = b/a
#             stack.append(c)
#     print(f'#{tc} {stack[-1]}')




icp = {'+':1,'-':1,'*':2,'/':2,'(':3}
isp = {'+':1,'-':1,'*':2,'/':2,'(':0}

for tc in range(1,11):
    N = int(input())
    data = input()
    stack = []
    text = ''

    for i in range(N):
        if '0'<=data[i]<='9':
            text += data[i]
        else:
            if data[i] == ')':
                while True:
                    if stack[-1] == '(':
                        stack.pop()
                        break
                    text += stack.pop()
            else:
                if len(stack)>0 and icp[data[i]] <= isp[stack[-1]]:
                    text += stack.pop()
                stack.append(data[i])
    while stack:
        text += stack.pop()
    print(text)
    stack = []
    n = len(text)

    for i in range(n)
        