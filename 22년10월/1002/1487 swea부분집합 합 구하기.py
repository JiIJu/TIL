def nCr(n):
    case = []
    for i in range(1<<N):
        result = []
        for j in range(N):
            if i & (1<<j):
                result.append(data[j])
        if sum(result)==W:
            case.append(result)

    return case

T = int(input())

for tc in range(1,T+1):
    N,W = map(int,input().split())
    data = list(map(int,input().split()))
    a=nCr(N)
    print(len(a))