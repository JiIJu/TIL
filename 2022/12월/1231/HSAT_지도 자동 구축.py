# HSAT 지도 자동 구축

N = int(input())

num = [0]*(N+1)
num[0] = 2
temp = 1

for i in range(1,N+1):
    num[i] = num[i-1]+temp
    temp *=2
print(num[N]**2)