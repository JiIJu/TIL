# 이코테 시각

N = int(input())

hour = 0
minute = 0
second = 0
n=0
cnt = 0
while hour<N+1:
    hour = n//3600
    a = str(hour)
    n = n - 3600*hour
    minute = n//60
    b = str(minute)
    n = n-60*minute
    second = n
    c = str(second)
    if ('3' in a or '3' in b or '3' in c):
        cnt+=1
    n = hour*3600 + minute*60 + second + 1
print(cnt)