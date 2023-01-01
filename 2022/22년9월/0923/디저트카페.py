
def dessert(x,y,p,r,l,cnt): # x,y 시작위치 p 방향설정 , r,l 오른쪽왼쪽 아래로 내려간 횟수
    global mcnt , ans

    if ans ==1:
        return
    if p == 0:
        if x+1<N and y-1>=0 and visited[data[x+1][y-1]]==0:
            visited[data[x+1][y-1]] = 1
            dessert(x+1,y-1,p,r+1,l,cnt+1)
            visited[data[x+1][y-1]] = 0
    elif p==1:

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    mcnt = 0
    data= [list(map(int,input().split())) for _ in range(N)]
    di = [-1,-1,1,1]
    dj = [1,-1,-1,1]
    visited = [0] * 101
    for i in range(N):
        for j in range(N):
            cnt = 1
            visited[data[i][j]] = 1

    print(mcnt)