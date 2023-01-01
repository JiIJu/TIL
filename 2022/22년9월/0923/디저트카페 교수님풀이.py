T = int(input())

dr = [1,1,-1,-1]
dc = [1,-1,-1,1]

RD = 0 # right down
LD = 1 # left down
LU = 2 # left up
RU = 3 # right up


def travel(visited,dir,now):
    global answer

    # now가 시작위치랑 같아지고 , 방향이 RU이면
    # 도착했따!!!!!!!!!!
    if now == start and dir == RU:
        answer = max(answer,len(visited))


    # 갈 수 있는 방향
    # 현재 방향으로 쭉 가거나
    # 다음방향으로 꺾어서 가거나
    # 방향이 바뀌는 순서는 RD,LD,LU,RU

    for d in range(2): # 을 더하면 다음방향 , 0이면 현재방향 유지
        dir +=d

        if dir>3:
            break

        nr = now[0] + dr[dir]
        nc = now[1] + dc[dir]
        # 다음위치로 가는데 다음위치가 범위 안이고
        # 전에 먹었던 디저트의 종류가 없어야 이동 가능
        if 0<=nr<N and 0<=nc<N and cafe_map[nr][nc] not in visited:
            visited.append(cafe_map[nr][nc])
            travel(visited,dir,(nr,nc))
            visited.remove(cafe_map[nr][nc])


for tc in range(1,T+1):
    N = int(input())

    cafe_map = [list(map(int,input().split())) for _ in range(N)]

    answer = -1

    for i in range(N):
        for j in range(N):
            start = (i,j) # 시작위치
            visited = [] # 내가 먹은 디저트 종류를 저장할 배열
            travel(visited,RD,(i,j))

    print(f'#{tc} {answer}')