def rps(i,j,n,m):
    if n == 1 and m == 2:
        return j
    elif n==1 and m ==3:
        return i
    elif n==1 and m==1:
        return i
    elif n == 2 and m == 2:
        return i
    elif n == 2 and m == 3:
        return j
    elif n == 2 and m == 1:
        return i
    elif n == 3 and m == 2:
        return i
    elif n == 3 and m == 3:
        return i
    elif n == 3 and m == 1:
        return j


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = list(map(int,input().split()))
    winner = []
    for i in range(0, N//2, 2):
        if N//2 %2 ==0:
            winner.append(rps(i, i + 1, data[i], data[i + 1]))
        else:
            if i == (N//2-1):
                winner.append(rps(i,i,data[i],data[i]))
            else:
                winner.append(rps(i, i + 1, data[i], data[i + 1]))
    for i in range(N//2, N ,2):
        if (N // 2) % 2 == 0:
            winner.append(rps(i, i + 1, data[i], data[i + 1]))
        else:
            if i == N - 1:
                winner.append(rps(i, i, data[i], data[i]))
            else:
                winner.append(rps(i, i + 1, data[i], data[i + 1]))
    ans = 0
    while True:
        s = []
        if len(winner) == 2:
           ans = rps(winner[0],winner[1],data[winner[0]],data[winner[1]])
           break
        b = len(winner)

        for i in range(0, b // 2, 2):
            if (b // 2) % 2 == 0:
                s.append(rps(winner[i], winner[i + 1], data[winner[i]], data[winner[i + 1]]))
            else:
                if i == (b // 2 - 1):
                    s.append(rps(winner[i], winner[i], data[winner[i]], data[winner[i]]))
                else:
                    s.append(rps(winner[i], winner[i + 1], data[winner[i]], data[winner[i + 1]]))
        for i in range(b // 2, b, 2):
            if (b // 2) % 2 == 0:
                s.append(rps(winner[i], winner[i + 1], data[winner[i]], data[winner[i + 1]]))
            else:
                if i == (b - 1):
                    s.append(rps(winner[i], winner[i], data[winner[i]], data[winner[i]]))
                else:
                    s.append(rps(winner[i], winner[i + 1], data[winner[i]], data[winner[i + 1]]))
        winner = []
        for i in range(len(s)):
            winner.append(s[i])
    print(f'#{tc} {ans+1}')