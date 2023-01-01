T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = [[] for _ in range(N)]

    for i in range(N):
        A , B = map(int,input().split())
        if A>B:
            A,B = B,A

        data[i] += [A]
        data[i] += [B]
    room = [0] * 401

    for i in range(N):
        if data[i][0] %2 ==0:
            data[i][0] = data[i][0]-1
        if data[i][1] %2 ==1:
            data[i][1] = data[i][1] +1
    for i in range(N):
        for j in range(data[i][0],data[i][1]+1):
            room[j] +=1
    max = 0
    for i in range(401):
        if room[i]>max:
            max = room[i]

    print(f'#{tc} {max}')
