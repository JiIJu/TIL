T = int(input())

for tc in range(1,T+1):

    N = int(input())
    num = [0]*5001
    bus = [[] for _ in range(N)]
    for i in range(N):
        A , B = map(int,input().split())
        bus[i] += [A]
        bus[i] += [B]
    P = int(input())
    stop = []
    for i in range(P):
        C = int(input())
        stop+= [C]
    for i in range(N):
        for j in range(bus[i][0],bus[i][1]+1):
            num[j] +=1
    print(f'#{tc}',end='')
    a =''
    for i in range(P):
        a += f' {num[stop[i]]}'
    print(a)