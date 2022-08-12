for tc in range(1,11):
    test = int(input())
    p = input()
    t = input()
    M = len(p)
    N = len(t)

    i = 0
    j = 0
    count=0


    while j<M and i < N:
        if t[i] != p[j]:
            i = i-j
            j = -1
        i += 1
        j += 1
        if j == M:
            count +=1
            j = 0
            i +=1
    print(f'#{tc} {count}')

    # while j<a_len and i <b_len:
    #
    #     if b[i] != a[j]:
    #         i = i - j
    #         j = -1
    #     i = i + 1
    #     j = j + 1
    #     if j == a_len:
    #         count+=1
    #         j =0
    #         i +=1
    # print(f'#{tc} {count}')