# 16953 A->B

def bfs(n):
    q = [(n,1)]
    while q:
        a,cnt = q.pop(0)
        for d in range(2):
            if d == 0:
                na = a*2
            else:
                na = (a*10)+1
            if na<=B:
                q.append((na,cnt+1))
                if na==B:
                    ans.append(cnt+1)
                    continue

A , B = map(int,input().split())
ans = []
bfs(A)
if ans:
    print(min(ans))
else:
    print(-1)
