T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = list(map(int,input().split()))

    # for i in range(a):
    #     for j in range(a-i-1):
    #         if data[j]>data[j+1]:
    #             data[j],data[j+1] = data[j+1],data[j]
    count = [0]*(51)
    b = [0] * N

    for i in range(N):
        count[data[i]] +=1
    for i in range(1,51):
        count[i] += count[i-1]
    for i in range(N-1,-1,-1):
        count[data[i]] -= 1
        b[count[data[i]]] = data[i]


    print(f'#{tc}',end=' ')
    for i in b:
        print(f'{i}',end=' ')
    print()