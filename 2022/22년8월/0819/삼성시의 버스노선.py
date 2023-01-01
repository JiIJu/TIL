T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    P = int(input())
    Ci = []
    result = 0
    count = []
    for i in range(P):
        Ci.append(int(input()))


    bus = [[] for _ in range(N)]
    # bus = [0] * 5000
    # stop = [0] * 5000
    for i in range(N):
        for j in range(data[i][0],data[i][1]+1):
            bus[i].append(j)

    for i in range(P):
        result = 0
        for j in range(N):
            # if bus[j][0]<=Ci[i]<=bus[j][1]:
            if Ci[i] in bus[j]:
                result+=1
        count.append(result)
    a =''
    print(f'#{tc}',end='')
    for i in range(P):
        a += f' {count[i]}'
    print(a)