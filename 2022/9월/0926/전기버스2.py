def backtracking(idx,cnt):
    global min_
    if min_<=cnt:
        return

    if idx>=N-1:
        min_ = min(min_,cnt)
        return
    for i in range(1,battery[idx]+1):
        backtracking(idx+i , cnt+1)


T = int(input())

for tc in range(1,T+1):

    data = list(map(int,input().split()))
    min_ = 9999
    N = data[0]
    battery = data[1:] + [0]
    backtracking(0,0)
    print(f'#{tc} {min_-1}')