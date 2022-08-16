T = int(input())

for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    M = len(str1)
    N = len(str2)
    i , j = 0 , 0

    while i<N and j<M:
        if str1[j] != str2[i]:
            i = i - j
            j = -1
        j +=1
        i +=1
    if j == M:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')