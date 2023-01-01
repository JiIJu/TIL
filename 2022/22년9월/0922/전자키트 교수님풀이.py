T = int(input())

def patrol(now,e_sum):
    global min_value
    if e_sum>min_value:
        return
    # 모든방을 방문했으면 시작지점으로 돌아간다.
    # 시작지점까지 걸리는 양 추가해서 최소값을 계싼
    if 0 not in visited:
        min_value = min(min_value,e_sum + e[now][0])
        return
    # 현재위치에서 갈수있는 다음방을 탐색
    for next_room in range(N):
        if next_room != now and visited[next_room] == 0:
            # 다음방으로 갔다고 체크하고 길을 찾는다.
            visited[next_room] = 1
            # 합을 최신화 한 다음 재귀 호출
            patrol(next_room,e_sum + e[now][next_room])
            # 방문체크 해제
            visited[next_room] = 0


for tc in range(1,T+1):
    N = int(input())

    e = [list(map(int,input().split())) for _ in range(N)]

    visited = [0] * N
    visited[0] = 1

    min_value = 11111
    patrol(0,0)
    print(min_value)