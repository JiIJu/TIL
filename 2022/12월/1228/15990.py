# 15990 1,2,3 더하기 5

T = int(input())
num = [[0,0,0] for i in range(100001)]
num[1],num[2],num[3],num[4] = [1,0,0],[0,1,0],[1,1,1],[2,0,1]
for i in range(5,100001):
    num[i][0] = (num[i-1][1]+num[i-1][2])%1000000009
    num[i][1] = (num[i - 2][0] + num[i - 2][2])%1000000009
    num[i][2] = (num[i - 3][0] + num[i - 3][1])%1000000009
for tc in range(T):
    n = int(input())
    print(sum(num[n])%1000000009)
