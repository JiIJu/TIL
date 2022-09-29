def perm(i, k):
    if i == k: #인덱스 i == 원소의 개수
        a = [0] + p[:] + [0]
        ans.append(a)
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            perm(i+1, k)
            p[i], p[j] = p[j], p[i]


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]

    min = 99999
    p=[]

    for i in range(1,N):
        p.append(i)
    ans = []
    perm(0,N-1)

    for i in range(len(ans)):
        sum = 0
        for j in range(len(ans[i])-1):
            sum+=data[ans[i][j]][ans[i][j+1]]
        if sum<min:
            min = sum
    print(f'#{tc} {min}')