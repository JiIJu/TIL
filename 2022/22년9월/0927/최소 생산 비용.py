

# row_num =  현재행에서 단계
# select = 중복체크
# price : 가격의 합

def backtracking(row_num , selected , price):
    global min_v

    if min_v < price:
        return
    # N개 골랐고 row_num 이 인덱스의 범위를 벗어났다면 계산
    if len(selected) == N and row_num==N:
        min_v = min(min_v , price)
        return

    # i : 열 번호
    for i in range(N):
        # 현재 row_num 행에서 i 열을 골랐다면,
        # row_num +1 행으로 넘어가서 i 열을 제외한 열을 골라보자
        if i not in selected:
            selected.append(i)
            backtracking(row_num+1,selected,price+V[row_num][i])
            selected.remove(i)

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    i,j = 0,0
    V = [list(map(int,input().split())) for _ in range(N)]
    min_v = 99999

    backtracking(0,[],0)
    print(f'#{tc} {min_v}')