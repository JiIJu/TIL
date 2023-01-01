# 9461 파도반수열


T = int(input())

for tc in range(T):
    n = int(input())
    data = [0] * 101
    data[1],data[2],data[3] = 1,1,1
    for i in range(4,101):
        data[i] = data[i-3]+data[i-2]
    print(data[n])