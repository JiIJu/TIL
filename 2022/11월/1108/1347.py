# 1347 미로만들기

N = int(input())
data = list(input())


dx = [1,0,-1,0]
dy = [0,-1,0,1]

d = 0
position = [0,0]
x_list = [0]
y_list = [0]
for i in range(N):
    if data[i] == 'R':
        d = (d+1)%4
    elif data[i] == 'L':
        d= (d+3)%4
    elif data[i] =='F':
        x,y = position[0],position[1]
        nx , ny = x+dx[d] , y+dy[d]
        x_list.append(nx)
        y_list.append(ny)
        position = [nx,ny]
max_x,max_y,min_x,min_y = max(x_list),max(y_list),min(x_list),min(y_list)
M,N = (max_x-min_x)+1 , (max_y-min_y)+1
sx,sy = abs(min_x),abs(min_y)
maze = [['#']*N for _ in range(M)]

for i in range(len(x_list)):
    maze[sx+x_list[i]][sy+y_list[i]]='.'
# print(maze)
for i in maze:
    print(''.join(i))