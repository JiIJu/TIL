for tc in range(1,11):
    t = int(input())
    data = list(map(int,input().split()))

    q = []
    a = 0
    ans =0
    while True:

        for i in range(1,6):
            a = data.pop(0)

            if a-i>0:
                data.append(a-i)
            else:
                data.append(0)
                ans = 1
                break
        if ans==1:
            break
    print(f'#{tc}',end=' ')
    print(*data)
