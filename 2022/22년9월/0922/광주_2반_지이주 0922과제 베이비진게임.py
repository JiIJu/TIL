T = int(input())

for tc in range(1,T+1):
    data = list(map(int,input().split()))

    player1 = []
    player2 = []
    for i in range(0,12,2):
        player1.append(data[i])
        player2.append(data[i+1])

    num1 = [0] * 10
    num2 = [0] * 10
    ans = 0
    for i in range(6):
        num1[player1[i]] += 1
        if max(num1) >=3:
            ans = 1
            break
        for j in range(8):
            if num1[j]>=1 and num1[j+1]>=1 and num1[j+2]>=1:
                ans =1
                break
        if ans !=0:
            break
        num2[player2[i]] += 1
        if max(num2) >=3:
            ans = 2
            break
        for j in range(8):
            if num2[j]>=1 and num2[j+1]>=1 and num2[j+2]>=1:
                ans =2
                break
        if ans!=0:
            break


    print(f'#{tc} {ans}')