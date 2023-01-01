T = int(input())

for tc in range(1,T+1):
    data , N = input().split()
    N = int(N)
    n = len(data)
    a = set([data])
    b = set()
    for i in range(N):
        while a:
            ans = a.pop()
            ans = list(ans)
            for j in range(n-1):
                for k in range(j+1,n):
                    ans[j] , ans[k] = ans[k] , ans[j]
                    b.add(''.join(ans))
                    ans[k] , ans[j] = ans[j] , ans[k]
        a,b = b,a
    print(f'#{tc} {max(a)}')