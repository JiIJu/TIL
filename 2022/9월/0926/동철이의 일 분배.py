
def backtracking(row_num,percent):
    global max_p
    if max_p>percent:
        return
    if row_num==N:
        max_p = max(max_p,percent)
        return

    for i in range(N):
        if visit[i]==0 and data[row_num][i] !=0:
            visit[i]=1
            backtracking(row_num+1,percent*data[row_num][i]*0.01)
            visit[i]=0


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    visit = [0]*(N)
    data = [list(map(int,input().split())) for _ in range(N)]
    max_p = -1
    backtracking(0,1)
    print(f'#{tc} {round(max_p*100,6)}')

    # '#%d %6f