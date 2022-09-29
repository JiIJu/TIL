T = int(input())

# 버스가 가면서 배터리 충전하는 함수
# idx는 정류장의 위치, cnt는 충전횟수
def bus(idx, cnt):
    global result
    # 시간초과를 피하기 위해서 더 작은 값이 안나오면 중지
    if cnt >= result:
        return
    # 만약 목적지를 넘는다면
    if idx >= N -1:
        # 지금 센 횟수랑 결과값이랑 비교해서 작다면 갱신
        if cnt <= result:
            result = cnt
        return
    # 한번 충전해서 갈수 있는 곳을 다 둘러보는 반복문
    # 해당 정류장에서 해당하는 배터리로 갈수 있는 경우의 수를 모두 둘러본다.
    for i in range(info[idx]):
        # 그 경우의 수에 해당하는곳으로 옮겨서 다시 살펴보자
        # i가 0부터 시작하니까 1씩 더 더한다.
        bus(idx+i+1, cnt +1)

for tc in range(1, T+1):
    info = list(map(int, input().split()))
    N = info.pop(0)
    result = 10000
    # 최초 들어갈때 충전을 한다고 가정하므로 cnt에 -1을 넣어준다.
    bus(0, -1)

    print("#{} {}".format(tc, result))