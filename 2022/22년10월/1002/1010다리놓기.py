def fact(n):
    if n<2:
        return 1
    else:
        return fact(n-1)*n
T = int(input())
for tc in range(1,T+1):
    N , M =  map(int,input().split())

    print(fact(M)//(fact(N)*fact(M-N))) # 순열
    # 순열을 코들로 재현하니 시간초과가 뜸 뭐시여 이게!!!