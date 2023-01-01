T = int(input())

for tc in range(1,T+1):
    two = list(input())
    thr = list(input())

    now_two = 0
    now_thr = 0
    # print(two , thr)
    # for i in range(len(two)-1,-1,-1):
    #     two[i] = int(two[i])
    #     now_two += int(two[i]) * 2**(len(two)-i-1)
    #
    # for i in range(len(thr)-1,-1,-1):
    #     thr[i] = int(thr[i])
    #     now_thr += int(thr[i]) * 3**(len(thr)-i-1)
    tmp_two , tmp_thr = 0,0
    # print(now_two , now_thr)
    ans = 0
    for i in range(len(thr)-1,-1,-1):
        for j in range(3):
            if thr[i] != j:
                tmp_thr = thr[i]
                thr[i]=j
                # print(thr)
            now_thr = 0
            for k in range(len(thr)-1, -1, -1):
                now_thr += int(thr[k]) * 3 ** (len(thr) - k - 1)
                # print(now_thr)

            for k in range(len(two)-1,-1,-1):
                for l in range(2):
                    if two[k] != l:
                        tmp_two = two[k]
                        two[k] = l
                    now_two = 0
                    for a in range(len(two) - 1, -1, -1):
                        now_two += int(two[a]) * 2 ** (len(two) - a - 1)
                    # print(now_two , now_thr)
                    if now_two == now_thr:
                        ans = 1
                        break
                    else:
                        thr[i] = tmp_thr
                        two[k] = tmp_two
                if ans ==1:
                    break
            if ans == 1:
                break
        if ans == 1:
            break

    # print(two , thr)
    print(f'#{tc} {now_thr}')