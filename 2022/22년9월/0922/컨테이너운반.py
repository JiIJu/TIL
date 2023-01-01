

T = int(input())

for tc in range(1,T+1):
    N , M = map(int,input().split()) # N = 컨테이너  M = 트럭
    w = list(map(int,input().split())) # w = 화물무게 t = 트럭적재용량
    t = list(map(int,input().split()))
    w = sorted(w)
    t = sorted(t)
    case = []
    for i in range(M-1,-1,-1):
        for j in range(N-1,-1,-1):
            if t[i]>=w[j]:
                case.append(w[j])
                w[j] = 99999
                break
    print(f'#{tc} {sum(case)}')