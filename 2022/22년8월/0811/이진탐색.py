T = int(input())

for tc in range(1,T+1):
    P,A,B = map(int,input().split())
    p = P
    countA = 0
    countB = 0
    a = 1
    b = 1
    c = 0

    while c != A:
        c = int((a+P)/2)
        countA += 1
        if A>c:
            a = c
        elif A<c:
            P = c

    c = 0

    while c != B:
        c = int((b+p)/2)
        countB += 1
        if B>c:
            b = c
        elif B<c:
            p = c


    if countA<countB:
        print(f'#{tc} A')
    elif countA>countB:
        print(f'#{tc} B')
    elif countA==countB:
        print(f'#{tc} 0')