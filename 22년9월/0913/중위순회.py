def inorder(n):
    global ans
    if n:
        inorder(c1[n])
        ans+=heap[n]
        inorder(c2[n])

for tc in range(1,11):
    N = int(input())
    data = []
    for i in range(N):
        data.append(list(input().split()))

    heap = [0] * 100
    ans = ''
    c1 = [0] * (N+2) # 왼
    c2 = [0] * (N+2) # 오
    for i in range(N):
        heap[i+1] = data[i][1]
        if len(data[i])==4:
            c1[int(data[i][0])] = int(data[i][2])
            c2[int(data[i][0])] = int(data[i][3])
        elif len(data[i]) ==3:
            c1[int(data[i][0])] = int(data[i][2])

    inorder(1)
    print(f'#{tc} {ans}')
