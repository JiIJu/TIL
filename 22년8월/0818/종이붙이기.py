T = int(input())

def func(N):
    if N == 20:
        return 3
    elif N == 10:
        return 1
    else:
        return func(N-10) + func(N-20)*2


for tc in range(1,T+1):
    N = int(input())
    data = [0] * 301
    data[10] = 1
    data[20] = 3

    print(f'#{tc} {func(N)}')
