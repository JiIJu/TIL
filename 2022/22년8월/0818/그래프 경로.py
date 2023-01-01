T = int(input())

for tc in range(1,T+1):
    V , E = map(int,input().split())
    data = [[0]*(V+1) for _ in range(V+1)]
    inp = [list(map(int,input().split())) for _ in range(E)]
    for i in range(1,V+1):
        for j in range(E):
            if i == inp[j][0]:
                data[i][inp[j][1]] += 1
            # if i == inp[j][1]:
            #     data[i][inp[j][0]] +=1
    S , G = map(int,input().split())
    v=S
    stack = []
    visit = [0] * (V+1)
    visit[v] = 1
    while True:
        for i in range(1,V+1):
            if data[v][i] == 1 and visit[i] ==0:
                stack.append(v)
                v = i
                visit[i] = 1
                break

        else:
            if len(stack) !=0 :
                v = stack.pop()
            else:
                break
    print(visit)
    if visit[G] != 0:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')

# [[0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 1, 1, 0, 0],
#  [0, 0, 0, 1, 0, 1, 0],
#  [0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 1],
#  [0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0]]