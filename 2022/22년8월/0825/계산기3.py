

#  연산자의 우선순위

icp = {'+':1,'*':2,'(':3}
isp = {'+':1,'*':2,'(':0}


def get_postfix(infix,n):
    postfix =''
    stack = []

    for i in range(n):
        if '0'<=infix[i]<='9':
            postfix += infix[i]
        else:
            # 연산자일 때
            # 닫는괄호일 경우 => 여는 괄호가 나올때까지 연산자를 모두 pop
            # 괄호가 아닐경우 => 자기 자신이 스택안에 있는 것보다 우선순위가 높아질 때 까지 pop
            if infix[i] == ')':
                while stack:
                    char = stack.pop()
                    if char == '(':
                        break
                    postfix += char
            else:
                while stack and icp[infix[i]]<=isp[stack[-1]]:
                    postfix += stack.pop()
                # 이제 내 우선순위가 높거나 스택에 아무것도 남지않았다 => push
                stack.append(infix[i])
        while stack:
            # 남은연산자 처리
            postfix += stack.pop()
        return postfix

def get_result(postfix):
    stack = []

    for c in postfix:
        if '0'<=c<='9':
            stack.append(int(c))
        else:
            right = stack.pop()
            left = stack.pop()

            if c =='+':
                result = right+left
            elif c == '*':
                result = right*left

        stack.append(result)
    return stack.pop()

T = 10

for tc in range(1,T+1):
    n = int(input())

    exp = input()

    postfix = get_postfix(exp,n)
    a = get_result(postfix)
    print(f'#{tc} {a}')