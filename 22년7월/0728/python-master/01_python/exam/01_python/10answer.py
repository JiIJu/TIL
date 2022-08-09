# 여러번 움직인 다음에
# 움직인 후의 위치를 출력해주는 함수
# 움직인 후의 위치가 범위를 벗어난다면 None을 반환


def get_final_position(N, mat, moves):
    # N : 행, 열의 크기
    # mat : 2차원 리스트, 평면을 나타내고 원소가 1인 경우 현재 위치이다.
    # moves : 움직일 방향이 들어있는 리스트

    # 1. 움직이기 전에 현재 위치가 어디인지를 알아야한다.
    now = [0, 0]

    # 2차원 리스트를 순회하면서 원소의 값이 1일때
    # 현재 위치를 최신화
    for x in range(N):
        for y in range(N):
            if mat[x][y] == 1:
                now = [x, y]

    # 현재 위치를 구했으니 moves 에 있는 정보대로 움직이면 된다.

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for move in moves:
        # 현재 x의 위치는 now[0] ,
        now[0] += dx[move]
        # 현재 y의 위치는 now[1]
        now[1] += dy[move]

        # 이동하고 난 다음의 위치가 범위를 벗어나면 return None
        if now[0] < 0 or now[0] >= N or now[1] < 0 or now[1] >= N:
            return None

    return now
