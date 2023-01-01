T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    data = list(map(int,input().split()))
    stack = []
    n = len(data)
    num = 0
    a = 0
    b = 0
    count = 0
    for i in range(N):
        stack.append((data[i],i))
    while True:
        a,num = stack.pop(0)
        a = a//2
        if a>0:
            stack.append((a,num))
        else:
            if N+b<M:
                stack.append((data[N+b],N+b))
                b += 1

        if len(stack)==0:
            break

    print(f'#{tc} {num+1}')