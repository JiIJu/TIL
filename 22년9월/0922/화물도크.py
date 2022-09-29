# def max_time(s,cnt):
#     global max_value
#     for i in range(1,N-s):
#         if data[s][1] <=data[s+i][0]:
#             for a in range(1,N-s-1):
#                 if data[s+1][1]<=data[s+1+a][0]:
#                     max_time(s+1+a,cnt+1)
#
#         if cnt>max_value:
#             max_value=cnt

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]


    for i in range(N-1):
        for j in range(i,N):
            if data[i][1]>data[j][1]:
                data[i] , data[j] = data[j] , data[i]
    # print(data)
    cnt = 1
    max_value = 0
    end = data[0][1]

    for i in range(1,N):
        if end<=data[i][0]:
            cnt+=1
            end = data[i][1]
    print(f'#{tc} {cnt}')
    # max_time(0,0)
    # print(max_value)