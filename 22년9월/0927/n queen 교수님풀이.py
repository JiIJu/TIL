
# 행 하나 증가 => 상태공간트리의 단계 증가
# 다음 행으로 간다 => 트리의 다음단계로 간다.
# board : 퀸이 놓인 상태
# remain : 남은 퀸 개수
def backtracking(row_num , board , remain):
    global cnt

    #현재 행에서 i번째 열에 퀸을 놓을 수 있는가?
    for i in range(N):
        can_place = True
        # 세로로 퀸이 있는지 검사
        for j in range(row_num):
            if board[i][j] == 1:
                can_place = False
                break
        # 대각선으로 퀸이 있는지 검사
        for j in range(1,row_num+1):
        # 왼쪽위 , 오른쪽 위
            pass
        if can_place == True:
            board[row_num][i] = 1
            backtracking(row_num+1,board,remain-1)
            board[row_num][i] = 0

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    cnt = 0 # 경우의수

    board =[[0]*8 for _ in range(8)]

    backtracking(0,board,N)
    print(f'#{tc} {cnt}')