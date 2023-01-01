# T = int(input())

# for i in range(1,T+1):
#     num = int(input())
#     data = list(map(int,input().split()))
#     a = [0] * 101
#     for j in range(1000):
#         a[data[j]] += 1
#     max = 0
#     maxnum = 0
#     for j in range(101):
#         if a[j]>=max:
#             max = a[j]
#             maxnum = j
#     print(f'#{num} {maxnum}')



# for i in range(1,11):
#     T = list(map(int,input().split()))
#     count =0
#     for j in range(2,len(T)-2):
#         if T[j]>T[j-1] and T[j]>T[j-2] and T[j]>T[j+1] and T[j]>T[j+2]:
#             max = [T[j-2],T[j-1],T[j+1],T[j+2]]
#             max.sort
#             count += T[j]-max[3]
#     print(f'{i} {count}')

for i in range(1,11):
    n = int(input())
    data = list(map(int,input().split()))
    for j in range(100):
    	for k in range(100-j-1):
            if data[k] > data[k+1]:
                data[k] , data[k+1] = data[k+1] , data[k]
    for a in range(n):
        data[0] += 1
        data[-1] -+ 1
        for j in range(100):
    	    for k in range(100-j-1):
                if data[k] > data[k+1]:
                    data[k] , data[k+1] = data[k+1] , data[k]
    print(f'#{i} {data[-1]-data[0]}')



# for i in range(1,11):
#     n = int(input())
#     data = list(map(int,input().split()))
#     print(data)
#     # data = sorted(data)
#     # for j in range(n):
#     #     data[j] -= 1
#     #     data[0] +=1
#     #     data = sorted(data)
#     # print(f'#{i} {data[99]-data[0]}')
