T = int(input())

for tc in range(T):

    # H = 호텔층수 W = 각층방수 N = 몇번째손님
    H,W,N = map(int,input().split())
    a = N//H +1
    f = N%H
    if N%H==0:
        a = N//H
        f = H
    print(f'{f*100+a}')