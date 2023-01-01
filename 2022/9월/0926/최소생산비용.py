def backtracking(row_num , price):
    global min_p

    if min_p<=price:
        return
    if row_num == N:
        min_p = min(min_p,price)
        return

    for i in range(N):
        if visit[i] ==0:
            visit[i]=1
            backtracking(row_num+1,price+data[row_num][i])
            visit[i]=0

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    min_p = 99999
    visit = [0] * N
    backtracking(0,0)
    print(f'#{tc} {min_p}')