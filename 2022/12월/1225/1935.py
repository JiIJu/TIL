# 1935 후위 표기식 2

N = int(input())
word = input()
num_list = [0]*N

for i in range(N):
    num_list[i] = int(input())

stack = []

for i in word:
    if 'A'<=i<='Z':
        stack.append(num_list[ord(i)-ord('A')])
    else:
        a = stack.pop()
        b = stack.pop()
        if i=='+':
            stack.append(b+a)
        elif i =='-':
            stack.append(b-a)
        elif i=='/':
            stack.append(b/a)
        elif i=='*':
            stack.append(b*a)
print("%.2f" %stack[0])