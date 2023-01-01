T = int(input())

for tc in range(1,T+1):
    E , N = map(int,input().split())
    data = input().split()
    case = []
    for i in range(0,E*2,2):
        case.append([int(data[i]),int(data[i+1])])
    # print(case)

    road = [0]*(E+2)
    cnt = 0
    for i in range(len(case)):
        road[case[i][1]] = case[i][0]
    print(road)
    for a in range(len(road)):
        for i in range(len(road)):
            # print(road[i])
            if road[i] == N:
                cnt +=1
                N = i
                break
    print(cnt+1)