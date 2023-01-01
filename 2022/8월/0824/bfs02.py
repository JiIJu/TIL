# 2차원 배열을 너비우선 탐색으로 탐색하는 bfs 함수를 작성
def bfs(si,sj,n): #n은 2차원 배열의 크기 n*n
    visited = [[0]*n for _ in range(n)] # 2차원 배열로 방문 체크
    queue = []
    i , j = si , sj
    visited[i][j] = 1
    queue.append((i,j))

    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    ni =0
    nj =0
    day = 0
    while queue:
        # 내가 현재 위치에서 방문을 몇번 할건지 구하자
        # 방문할 위치는 큐에 들어있고 그 위치의 개수를 구하면 된다.
        size = len(queue)

        # 탐색 횟수를 이전에 알아낸 큐의 크기만큼만 하도록 제한하면
        # 해당 일차에만 반복하도록 제한할 수 있다.
        # 2차원 배열 모양 출력
        print('==========')
        for k in range(n):
            print(visited[k])
        print('==========')
        print(day)
        for _ in range(size):

            #현재 방문 위치 꺼내기
            i,j = queue.pop(0)



            # 현재 위치에서 갈 수 있는곳 검사 ( 델타를 이용한 4방향 탐색)

            for d in range(4):

                # 다음위치 알아내기 (행,열)
                ni = i + di[d] # 다음행
                nj = j + dj[d] # 다음열
                # 다음위치가 탐색이 가능한 위치인지 검사 (배열 범위를 벗어나지는 않았는지 방문을 전에 한적이 있는지 검사)
                if 0<=ni<n and 0<=nj<n and visited[ni][nj] == 0:
                # 탐색이 가능한 위치면
                # 방문 체크를 하고
                    visited[ni][nj] = 1
                # 큐에 다음을 탐색하기 위해 큐에 다음 위치를 추가
                    queue.append((ni,nj))
        day+=1
n = 10
bfs(5,5,n)
print()