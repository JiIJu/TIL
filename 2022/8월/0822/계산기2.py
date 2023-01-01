# 피연산자 먼저 푸시 => 연산자 만나면 피연산자 두번pop

for tc in range(1,11):
    N = int(input())
    data = input()
    stack = [0]*N
    icp = {'+':1 , '-':1,'*':2,'/':2}
    ans = ''
    top = -1
    for i in range(N):
        if '0'<=data[i]<='9':
            ans += data[i]
        else:
            if top>-1 and icp[data[i]]<=icp[stack[top]]:
                ans += stack[top]
                top -=1
            top +=1
            stack[top] = data[i]
    while top>-1:
        ans += stack[top]
        top-=1

    a = []
    b=0
    c=0
    i = 0
    while i<N:
        if '0'<=ans[i]<='9':
            a += [int(ans[i])]
        else:
            b=a.pop()
            c=a.pop()
            d = 0
            if ans[i] == '+':
                d = int(c) + int(b)
            elif ans[i] == '-':
                d = int(c) - int(b)
            elif ans[i] == '*':
                d = int(c) * int(b)
            elif ans[i] == '/':
                d = int(c) / int(b)
            a.append(d)
        i +=1
    print(f'#{tc} {a[-1]}')


