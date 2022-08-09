#민석이의 과제체크하기

T = int(input())

for a in range(1,T+1):
    N , K = map(int,input().split())
    num = list(map(int,input().split()))
    data = [0]*(N+1)
    for i in range(K):
        data[num[i]] = 1
    lst = ''
    ilst = ''
    for i in range(1,N+1):
        if data[i] != 1:
            ilst += ' ' + str(i)
    print(f'#{a}{ilst}')