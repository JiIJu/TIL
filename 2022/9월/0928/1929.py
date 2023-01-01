M , N = map(int,input().split())

data = [0] * (N+1)
data[0],data[1] = 1,1
n = 2
while n<=N//2:          # N//2 보다 크면 2이상을 곱했을 때 어차피 N을 초과하므로 N//2까지만 확인
    for i in range(2,N+1):
        if i*n>=N+1:    # 가지치기!
            break
        if data[n*i] ==0:   # 배수는 소수가 아니므로 1을 넣어 소수가 아님을 표시
            data[n*i] = 1

    n+=1
for i in range(M,N+1):
    if data[i] == 0:
        print(i)
