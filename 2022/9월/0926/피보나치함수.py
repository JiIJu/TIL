def fib(n):
    global cnt1 , cnt2 , memo
    if n>=2 and len(memo)<=n:
        memo.append(fib(n-1)+fib(n-2))
    return memo[n]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cnt1 = 0
    cnt2 = 0
    memo = [0,1]
    fib(N)
    print(memo[N-1] , memo[N])