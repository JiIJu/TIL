for tc in range(1,11):
    T , N = map(int,input().split())
    data = input().split()
    case = []
    for i in range(0,N,2):
        case.append([int(data[i]),int(data[i+1])])
    stack = [0]
    n = len(case)
    while stack:
        for i in range(n):
            a = stack.pop()
            if case[i][0] == a:
