# 15988 1,2,3 더하기 3

T = int(input())
data = [0] *(1000001)
data[1] = 1
data[2] = 2
data[3] = 4
data[4] = 7
for tc in range(T):
    N = int(input())
    for i in range(5,N+1):
        data[i] = (data[i-3]+data[i-2]+data[i-1])%1000000009
    print(data[N])