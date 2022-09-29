def dessert(y, x, d, p, q, cnt):
    global max, flag
    if flag == 1:
        return
    if d == 0:
        if y + 1 < n and x + 1 < n and visit[arr[y + 1][x + 1]] == 0:
            visit[arr[y + 1][x + 1]] = 1
            dessert(y + 1, x + 1, d, p + 1, q, cnt + 1)
            visit[arr[y + 1][x + 1]] = 0
        dessert(y, x, 1, p, q, cnt)

    elif d == 1 and p > 0:
        if y + 1 < n and x - 1 > 0 and visit[arr[y + 1][x - 1]] == 0:
            visit[arr[y + 1][x - 1]] = 1
            dessert(y + 1, x - 1, d, p, q + 1, cnt + 1)
            visit[arr[y + 1][x - 1]] = 0
        dessert(y, x, 2, p, q, cnt)

    elif d == 2 and q > 0 and p > 0:
        if y - 1 > 0 and x - 1 >= 0 and visit[arr[y - 1][x - 1]] == 0:
            visit[arr[y - 1][x - 1]] = 1
            dessert(y - 1, x - 1, d, p - 1, q, cnt + 1)
            visit[arr[y - 1][x - 1]] = 0
        dessert(y, x, 3, p, q, cnt)
    elif d == 2 and q > 1:
        if y - 1 >= 0 and x + 1 > 0 and visit[arr[y - 1][x + 1]] == 0:
            visit[arr[y - 1][x + 1]] = 1
            dessert(y - 1, x + 1, d, p, q - 1, cnt + 1)
            visit[arr[y - 1][x + 1]] = 0
        dessert(y, x, 3, p, q, cnt)
    elif d == 3:
        return
    elif d == 2 and q == 1 and p == 0:
        if cnt > max:
            max = cnt
            flag = 1
            return


t = int(input())
for tc in range(1, t + 1):
    visit = [0] * 101
    n = int(input())
    max = -1
    arr = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n - 2):
        for j in range(1, n - 1):
            cnt = 0
            flag = 0
            visit[arr[i][j]] = 1
            dessert(i, j, 0, 0, 0, 1)
            visit[arr[i][j]] = 0
    print('#%d' % tc, max)