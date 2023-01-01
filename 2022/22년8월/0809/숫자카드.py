T = int(input())

for a in range(1,T+1):
    N = int(input())
    ai = input()
    data = [0]*10
    for i in range(10):
        for j in range(N):
            if i == int(ai[j]):
                data[i] += 1
    max=0
    idx=0
    for i in range(10):
        if data[i]>=max:
            max=data[i]
            idx=i
    for i in range(10):
        for j in range(10-i-1):
            if data[j]>data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
    print(f'#{a} {idx} {max}')
    
        #교수님 풀이

    T = int(input())

    for tc in range(1,T+1):
        N = int(input()) #숫자카드 개수
        number = input() # 숫자카드들이 주어지는데 공백없이 붙여서 출력

        count = [0] * 10

        for num in number:
            count[int(num)] += 1 #숫자카드 갯수새기

        max_count = 0
        number_max = 0
        for i in range(10):
            if count[i]>=max_count: #i카드가 등장한 횟수가 내가 지금 알고있는 최대 횟수보다 많으면 바꿔달라
                max_count = count[i]
                number_max = i
