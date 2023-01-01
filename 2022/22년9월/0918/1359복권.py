def fact(n):
    if n<2:
        return 1
    return n*fact(n-1)

def com(n,m):
    return fact(n)/(fact(m)*fact(n-m))

N , M , K = map(int,input().split())

# M C N * M C N
a = com(N,M)
a = a*a

cnt = 0
for i in range(K,M+1): # 5 4 1 // 1~4
    if N-M>=M-i:
        cnt += com(N,M)*com(M,i)*com(N-M,M-i)
#     print(com(N,M),com(M,i),com(N-M,M-i),cnt)
# print(cnt , a)
print(cnt/a)

