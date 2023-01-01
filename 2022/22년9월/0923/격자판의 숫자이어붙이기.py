def number(x,y,cnt,num):
    global ans
    if cnt ==6:
       if num not in ans:
           ans.append(num)
       return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<4 and 0<=ny<4:
            number(nx,ny,cnt+1,num*10+data[nx][ny])
            # x,y = nx, ny



T = int(input())

for tc in range(1,T+1):
    data = [list(map(int,input().split())) for _ in range(4)]

    dx = [1,-1,0,0]
    dy = [0,0,-1,1]

    ans = []

    for i in range(4):
        for j in range(4):
            number(i,j,0,data[i][j])
    print(f'#{tc} {len(ans)}')