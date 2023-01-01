# 14888 연산자 끼워넣기

def dfs(cnt,total,plus,minus,mul,divide):
    global maxV,minV
    if cnt==N-1:
        maxV = max(total,maxV)
        minV = min(total,minV)
        return
    if plus:
        dfs(cnt+1,total+data[cnt+1],plus-1,minus,mul,divide)
    if minus:
        dfs(cnt + 1, total - data[cnt + 1], plus , minus-1, mul, divide)
    if mul:
        dfs(cnt + 1, total * data[cnt + 1], plus, minus, mul-1, divide)
    if divide:
        if total<0 and data[cnt+1]>0:
            dfs(cnt + 1, abs(total) // data[cnt + 1] * -1, plus, minus, mul, divide-1)
        else:
            dfs(cnt + 1, total // data[cnt + 1], plus, minus, mul, divide-1)
N = int(input())
data = list(map(int,input().split()))
cal = list(map(int,input().split()))
maxV,minV = -10**9,10**9
dfs(0,data[0],cal[0],cal[1],cal[2],cal[3])
print(maxV)
print(minV)