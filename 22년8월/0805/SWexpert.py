 #1204

# T = int(input())

# for i in range(1,T+1):
#     case = int(input())
#     data = list(map(int,input().split()))
#     cnt = 0
#     max = 0
#     for j in range(len(data)):
#         if data.count(data[j])>cnt:
#             cnt = data.count(data[j])
#             max = data[j]
#     print(f'#{case} {max}')


#1954
# T = int(input())
# for i in range(1,T+1):
#     N = int(input())
#     snail = [[0]*N for _ in range(N)]
#     dx = [0 , 1 , 0 , -1]
#     dy = [1 , 0 , -1 , 0]
#     x,y = 0 , 0
#     k=0
#     for j in range(1,N*N +1):
#         snail[x][y] = j
#         x += dx[k]
#         y += dy[k]

#         if x<0 or y<0 or x>=N or y >=N or snail[x][y] !=0:
#             x -= dx[k]
#             y -= dy[k]
#             k = (k+1)%1
#             x += dx[k]
#             y += dy[k]
#     print(snail)
T = int(input())

for t in range(1, T+1):
    N = int(input())

    result = [[0]*N for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x = 0
    y = 0
    way = 0

    for n in range(1, N**2+1):
        result[x][y] = n
        x_ = x + dx[way]
        y_ = y + dy[way]

        if x_ not in range(N) or y_ not in range(N) or result[x_][y_] != 0:
            way = (way + 1) % 4

        x += dx[way]
        y += dy[way]
    print(f'#{t}')
    for i in result:
        print(*i)






