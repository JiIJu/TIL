def fact(n):
    if n<2:
        return 1
    else:
        return fact(n-1) * n

N , K = map(int,input().split())

ans = fact(N)//(fact(K)*(fact(N-K)))
print(ans)