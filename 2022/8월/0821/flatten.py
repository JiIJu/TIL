for tc in range(1,11):
    N = int(input())
    data = list(map(int,input().split()))

    ground = [0] * 101
    arr = [0] * 100
    for i in range(100):
        ground[data[i]] +=1
    for i in range(1,101):
        ground[i] += ground[i-1]
    for i in range(99,-1,-1):
        ground[data[i]] -= 1
        arr[ground[data[i]]] = data[i]
    print(arr)
    for j in range(N):
        ground = [0] * 101

        for i in range(100):
            ground[arr[i]] += 1
        for i in range(1, 101):
            ground[i] += ground[i - 1]
        for i in range(99, -1, -1):
            ground[arr[i]] -= 1
            arr[ground[arr[i]]] = arr[i]
        arr[0] += 1
        arr[-1] -= 1

print(f'#{tc} {arr[-1]-arr[0]}')
