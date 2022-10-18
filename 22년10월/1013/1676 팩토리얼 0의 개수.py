def fact(n):
    if n<2:
        return 1
    else:
        return fact(n-1)*n

N = int(input())
ans = fact(N)

str_ans = str(ans)

cnt = 0
for i in range(len(str_ans)-1,-1,-1):
    if str_ans[i]=='0':
        cnt+=1
    else:
        break
print(cnt)