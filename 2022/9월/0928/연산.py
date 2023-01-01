def check():
    ans = [0]*1000001
    ans[0] = [N,0]
    visit[N] = 1
    now = 0
    new = 0
    while ans:
        s,cnt = ans[now]
        if s==M:
            return cnt
        if s*2<=1000000 and visit[s*2] == 0:
            visit[s*2] = 1
            new +=1
            ans[new] = [s*2 , cnt+1]

        if 0<s-1 and visit[s-1] == 0:
            visit[s-1] = 1
            new += 1
            ans[new] = [s -1, cnt + 1]
        if s+1<=1000000 and visit[s+1]==0:
            visit[s+1] = 1
            new += 1
            ans[new] = [s +1, cnt + 1]
        if 0<s-10 and visit[s-10]==0:
            visit[s-10] = 1
            new += 1
            ans[new] = [s -10, cnt + 1]

        now+=1
T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    visit = [0] * 1000001
    q = check()
    print(f'#{tc} {q}')


