def inorder(n):
    global ans
    if n:
        inorder(road1[n])
        ans+=data[n-1][1]
        inorder(road2[n])
for tc in range(1,11):
    N = int(input())
    data = [list(input().split()) for _ in range(N)]

    road1 = [0]*(N+2)
    road2 = [0]*(N+2)
    ans = ''
    heap = [0]*100

    for i in range(N):
        # heap[i+1]=data[i][1]
        if len(data[i])==4:
            road1[int(data[i][0])] = int(data[i][2])
            road2[int(data[i][0])] = int(data[i][3])
        elif len(data[i])==3:
            road1[int(data[i][0])] = int(data[i][2])

    inorder(1)
    print(ans)