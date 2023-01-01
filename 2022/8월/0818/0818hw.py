for tc in range(1,11):
    T , N = map(int,input().split())

    data = [[0]*100 for _ in range(100)]
    a = list(map(int,input().split()))
    stack = []
    visit = [0]*100
    v = 0
    visit[v] = 1
    remember = 0
    for i in range(0,N*2,2):
        data[a[i]][a[i+1]] +=1
    while True:
        for i in range(100):
            if data[v][i] == 1 and visit[i] == 0:
                stack.append(v)
                v = i
                visit[i] = 1
                break
        else:
            if len(stack)!=0:
                v = stack.pop()
            else:
                break
    # print(data)
    if visit[-1] == 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')
#
# for tc in range(1):
#     T , N = map(int,input().split())
#
#     data = [[0]*20 for _ in range(20)]
#     a = list(map(int,input().split()))
#     stack = []
#     visit = [0]*20
#     v = 0
#     visit[v] = 1
#     for i in range(0,N,2):
#         data[a[i]][a[i+1]] +=1
#     while True:
#         for i in range(20):
#             if data[v][i] >= 0 and visit[i] ==0:
#                 stack.append(v)
#                 v = i
#                 visit[i] = 1
#                 break
#         else:
#             if len(stack)!=0:
#                 v = stack.pop()
#             else:
#                 break
#     print(visit)