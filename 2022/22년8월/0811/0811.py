# for tc in range(1,11):
#     N = int(input())
#     data = [list(map(int,input().split())) for _ in range(100)]
#     max = 0
#     for i in range(100):
#         sum = 0
#         for j in range(100):
#             sum += data[i][j]
#         if sum>max:
#             max = sum
#     for j in range(100):
#         sum = 0
#         for i in range(100):
#             sum += data[i][j]
#             if sum>max:
#                 max = sum
#     sum = 0
#     for i in range(100):
#         sum += data[i][i]
#     if sum>max:
#         max=sum
#     sum = 0
#     for i in range(100):
#         sum += data[i][100-i-1]
#     if sum>max:
#         max = sum
#     print(f'#{tc} {max}')


for tc in range(1,11):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(100)]
    max1 = 0
    max2= 0
    max3=0
    max4=0
    MAX=[]
    sum3 = 0
    sum4 = 0
    for i in range(100):
        sum1 = 0
        sum2 = 0

        sum3 += data[i][i]
        sum4 += data[i][99 - i]
        for j in range(100):
            sum1 += data[i][j]
            sum2 += data[j][i]

            if sum1>max1:
                max1 = sum1
            if sum2>max2:
                max2 = sum2
        if sum3>max3:
            max3 = sum3
        if sum4>max4:
            max4 = sum4

    print(f'#{tc} {max1} {max2} {max3} {max4}')