N,M = map(int,input().split())

listen = {}
see = {}
for i in range(N):
    listen[input()]=1
for i in range(M):
    see[input()]=1

ans = []

if N>=M:
    for i in listen:
        if i in see:
            ans.append(i)
else:
    for i in see:
        if i in listen:
            ans.append(i)
ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])