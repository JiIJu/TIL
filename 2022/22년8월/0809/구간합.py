T = int(input())

for a in range(1,T+1):
    N , M = map(int,input().split())
    ai = list(map(int,input().split()))
    data=[0]*(N-M+1)
    for i in range(N-M+1):
        for j in range(M):
            data[i] += ai[i+j]

    for i in range(len(data)):
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j] , data[j+1] = data[j+1] , data[j]
    print(f'#{a} {data[-1]-data[0]}')

#교수님 풀이 업로드

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    numbers = list(map(int,input().split()))
    
    #구간합의 최소,최대값
    max_sum = 0
    min_sum = 10000 * M
    
    for i in range(0,N-M+1):
        sub_sum = 0 #구간 합
        # M만큼 가면서 구간합을 구해준다.
        for j in range(0,M):
            sub_sum += numbers[i+j]
        max_sum = sub_sum if sub_sum>max_sum else max_sum
        min_sum = sub_sum if sub_sum>min_sum else min_sum
    print(f'#{tc} {max_sum-min_sum}
    
