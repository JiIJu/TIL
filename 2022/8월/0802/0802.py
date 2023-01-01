#1859 백만장자 프로젝트
# T = int(input())

# for i in range(1,T+1):
#     N = int(input())
#     data = list(map(int,input().split(" ")))
#     max_value = data[-1]
#     profit = 0
#     for j in range(N-2,-1,-1):
#         if data[j]>=max_value:
#             max_value = data[j]
#         if data[j]<max_value:
#             profit += max_value - data[j]
#     print(f'#{i} {profit}')

#1204 최빈수 구하기
T = int(input())
for i in range(1,T+1):
    data = list(map(int,input().split()))
    cnt = []
    for j in range(len(data)):
        cnt.append(data.count(data[i]))
    print(cnt)
