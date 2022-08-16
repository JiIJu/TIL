T = int(input())

for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    a = set(str1)
    a = list(a)
    count = 0
    max = 0

    for i in range(len(a)):
        count = 0
        for j in range(len(str2)):
            if str2[j] == a[i]:
                count+=1
            if max<count:
                max = count

    print(f'#{tc} {max}')