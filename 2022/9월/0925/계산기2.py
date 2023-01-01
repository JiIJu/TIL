def dfs(i,j,N):
    visited = [[0]*N for _ in range(N)] #2차원 방문 체크 배열
    global now
    stack = []
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    visited[i][j] = 1
    stack.append([i,j])
    while True:

        # 현재 위치를 방문했다고 체크

        # 현재 위치 i,j에서 갈수 있는곳 탐색
        # 2차원 배열에서는 상하좌우로 이동할 수 있다.
        for d in range(4):
            ni = di[d] + i
            nj = dj[d] + j
            # 다음 위치 정한 다음에 움직일 수 있는 지 알아보기
            # 벽이거나 2차원배열 범위 벗어나거나 방문한 적 있는 좌표여도 못감.
            if 0<=ni<N and 0<=nj<N and data[ni][nj] != 1 and visited[ni][nj] == 0:
                #갈 수 있는 위치
                #현재 위치를 스택에 저장
                #현재 위치를 다음위치로 최신화
                stack.append([now[0],now[1]])

                i,j = ni,nj
                visited[i][j] = 1

                now = [i,j]

                break
        else:
            #갈 수 있는 칸이 없으면
            #pop을 해서 뒤로 돌아간다.
            #stack이 비어있으면 반복을 종료
            if stack:
                now = stack.pop()
                i, j = now[0], now[1]

        print(stack)
        if now == finish:
            return len(stack)
        elif len(stack)==0:
            return 0
        # if now == finish:
        #     return now



T = int(input())

for tc in range(1,T+1):
    N = int(input())
    ans = 1
    data = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            data[i][j] = int(data[i][j])
    start = []

    finish = []
    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                start = [i,j]
    stack = []
    for i in range(N):
        for j in range(N):
            if data[i][j] == 3:
                finish = [i,j]

    a = dfs(start[0],start[1],N)
    if a==0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {a-2}')


