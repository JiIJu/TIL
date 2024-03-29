# 평면 좌표에서 현재 좌표와 이동하는 방향이 주어졌을때,
# 이동하고 난 후의 위치가 유효한 위치인지 알려주는 함수


def is_position_safe(N, M, position):
    # N : 행, 열의 크기
    # M : 이동하는 방향 (1칸씩 이동한다.)
    # position : 현재 위치를 말해주는 튜플 (0,0) => x= 0, y= 0 , 0행0열에 있다.
    x, y = position

    # M => 이동하는 방향
    # 0 ,1, 2, 3  : 상 하 좌 우
    if M == 0:  # 위로 움직인다.
        x += -1
    elif M == 1:  # 아래로 움직인다.
        x += 1
    elif M == 2:  # 왼쪽으로 움직인다.
        y += -1
    elif M == 3:  # 오른쪽으로 움직인다.
        y += 1

    # 리스트를 이용해서 방향을 표현하고, 그 리스트를 통해 이동을 바로 하는 방법
    # 조건문을 사용하지 않는 방법
    dx = [-1, 1, 0, 0]
    # dx[0] : x가 위로 움직이면 얼마나 변하나?? => 1 감소 => -1
    # dx[1] : x가 아래로 움직이면 얼마나 변하나?? => 1 증가 => 1
    # dx[2] , dx[3] : x가 왼쪽 또는 오른쪽으로 움직이면 행은 변화가 없음.. => 0
    dy = [0, 0, -1, 1]

    # M : 0 1 2 3 : 상 하 좌 우
    x += dx[M]
    y += dy[M]

    # 이동한 다음에 x, y 가 0,0 ~ N-1 , N-1 범위에 존재하는지 확인한다.
    if 0 <= x <= N - 1 and 0 <= y <= N - 1:
        return True
    else:
        return False
