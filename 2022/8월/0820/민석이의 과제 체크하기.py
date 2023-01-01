T = int(input())

for tc in range(1,T+1):
    N , K = map(int,input().split())
    student = list(map(int,input().split()))
    data = [0] * (N+1)
    no = []
    for i in range(K):
        data[student[i]] +=1
    for i in range(1,N+1):
        if data[i] == 0:
            no += [i]
    print(f'#{tc} ',end='')
    print(*no)