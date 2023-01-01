T = int(input())

for tc in range(T):
    n = int(input())
    cnt= [0]*(11)
    cnt[1] = 1
    cnt[2] = 2
    cnt[3] = 4
    for i in range(4,11):
        cnt[i] = cnt[i-3]+cnt[i-2]+cnt[i-1]
    print(cnt[n])


