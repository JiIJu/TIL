# T = int(input())
#
# for tc in range(1,T+1):
#     N , K = map(int,input().split())
#     data = [1,2,3,4,5,6,7,8,9,10,11,12]
#
#     count = 0
#
#     for i in range(1<<12):
#         sum = 0
#         for j in range(12):
#             if i & (1<<j):
#                 sum += data[j]
#         if sum == K:
#             print(sum)
#             count += 1
#
#     print(f'#{tc} {count}')

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    count = 0
    for i in range(1 << 12):
        sum = 0
        a = []
        for j in range(12):
            if i & (1 << j):
                a += [data[j]]
        count_len=0
        for j in a:
            count_len+=1
        if count_len == N:
            for j in range(N):
                sum += a[j]

        if sum == K:
            count+=1

    print(f'#{tc} {count}')

# arr = [3,6,7]
#
# n = len(arr)
#
# for i in range(1<<n):
#     for j in range(n):
#         if i & (1<<j):
#             print(arr[j] , end=', ')
#     print()
