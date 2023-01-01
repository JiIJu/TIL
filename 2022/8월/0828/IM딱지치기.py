N = int(input())
# 별 동그라미 네모 세모
# 4 3 2 1

for _ in range(0,2*N,2):
    data = [list(map(int,input().split())) for _ in range(2)]
    count1 = [0]*5
    count2 = [0]*5

    for i in range(2):
            for k in range(1,5):
                for j in range(1, len(data[i])):
                    if i ==0:
                        if k == data[0][j]:
                            count1[k] += 1
                    elif i == 1:
                        if k == data[1][j]:
                            count2[k] += 1

    for i in range(4,0,-1):
        if count1[i]>count2[i]:
            print('A')
            break
        elif count1[i]<count2[i]:
            print('B')
            break
        if i == 1 and count1[i]==count2[i]:
            print('D')


