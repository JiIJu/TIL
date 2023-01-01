# 1일차 6차시 min max
# T = int(input())
#
# for i in range(1, T + 1):
#     N = int(input())
#     ai = list(map(int, input().split()))
#
#     for j in range(N):
#         for k in range(N-j-1):
#             if ai[k] >= ai[k + 1]:
#                 ai[k], ai[k+1] = ai[k+1], ai[k]
#     print(f'#{i} {ai[N-1] - ai[0]}')

#1일차 7차시 전기버스
# N 정류장종점 M 충전기설치 정류장번호 K 한번충전으로 이동가능정류장

# T = int(input())
#
# for i in range(1,T+1):
#     K,N,M = map(int,input().split())
#     data = [0] * (N + K*10)
#     Mdata = list(map(int,input().split()))
#     for j in range(M):
#         data[Mdata[j]] = 1
#     n = 0
#     count=0
#     while n<N:
#         for j in range(K,-1,-1):
#             if j == 0:
#                 n = N
#                 count=0
#                 break
#             elif data[n+j] == 1:
#                 n += j
#                 count+=1
#                 break
#             elif n + j >= N:
#                 n += j
#                 break
#
#     print(f'#{i} {count}')


#서랍의 비밀번호
# P , K = map(int,input().split())
# if P>=K:
#     print(P-K+1)
# else:
#     print(1000-K+P)
#자릿수 더하기
# N = input()
# sum = 0
# for i in N:
#     sum += int(i)
# print(sum)

#최대수 구하기
# T = int(input())
#
# for i in range(1,T+1):
#     data = list(map(int,input().split()))
#     data.sort()
#
#     print(f'#{i} {data[len(data)-1]}')

#큰놈 , 작은놈 , 같은놈
# T = int(input())
#
# for i in range(1,T):
#     a , b = map(int,input().split())
#     if a>b:
#         print(f'#{i} >')
#     elif a==b:
#         print(f'#{i} =')
#     else:
#         print(f'#{i} <')

#전기버스 교수님 풀이
# def drive(K,N): #버스를 운행하는 함수
#
#     # return 0 : 충전소가 제대로 설치되어있지 않음
#     # return >0 : 충전소가 제대로 설치되어 있다.
#     last = 0 #마지막으로 충전했던 위치
#     next = K #버스가 최대로 이동한 위치
#     count = 0 #충전한 횟수
#
#     #종점에 도착할 때 까지 반복
#     while next < N:
#         # 버스가 이동한 위치에 충전기가 있나없나 검사
#         # 충전기가 없다면 뒤로 한칸씩 돌아가면서 찾을 때 까지 뒤로간다.
#         while stop[next] == 0:
#             next -= 1
#             if next == last:
#                 return 0
#
#         # 만약 뒤로 갔는데 내가 마지막으로 충전한 위치까지 와버렸다면
#         # 다시 앞으로 가봤자 다시 돌아올테니까 충전소가 제대로 설치되어 있지 않은것이다.
#
#     # 여기까지 왔다면 충전기가 제대로 설치되어 있다.
#     # 마지막 충전위치를 갱신
#     last = next
#     #다음 위치로 이동
#     next += K
#     # 충전횟수 증가
#     count +=1
# #N 보다 next가 크거나 같아졌으니 완주했다
#     return count
#
#
# T = int(input())
#
# for tc in range(1,T+1):
#     K,N,M = map(int,input().split())
#     # K : 이동할수있는거리
#     # N : 버스가 가야할 거리
#     # M : 충전기 개수
#     charge = list(map(int,input().split()))
#     stop = [0] * N
#     for x in charge: #x는 충전소가 있는 정류장의 위치
#         stop[x] = 1
#     answer = drive(K,N)
#     print(f'#{tc} {answer}')


#8차시 1일차 숫자카드

# T = int(input())
#
# for a in range(1,T+1):
#     N = int(input())
#     ai = input()
#     data = []
#     for i in ai:
#         data.append(i)
#     for i in range(N):
#         for j in range(N-i-1):
#             if data[j]>data[j+1]:
#                 data[j],data[j+1] = data[j+1],data[j]
#     result = 1
#     idx = 0
#     max = 0
#     max_data = []
#     idx_data = []
#     for i in range(N):
#         if data.count(data[i]) >= max:
#             max = data.count(data[i])
#             max_data.append(max)
#             idx = i
#             idx_data.append(idx)
#     for i in range(len(max_data)-1):
#         if max_data[i] == max_data[i+1]:
#             result = 0
#     if result ==0:
#         print(f'#{a} {data[idx_data[-1]]} {max}')
#     else:
#         print(f'#{a} {data[idx]} {max}')

#
# T = int(input())
#
# for a in range(1,T+1):
#     N = int(input())
#     ai = input()
#     data = []
#     for i in ai:
#         data += [i]
#     for i in range(N):
#         for j in range(N-i-1):
#             if data[j]>data[j+1]:
#                 data[j],data[j+1] = data[j+1],data[j]
#     result = 1
#     idx = 0
#     max = 0
#     max_data = []
#     idx_data = []
#     for i in range(N):
#         if data.count(data[i]) >= max:
#             max = data.count(data[i])
#             max_data += [max]
#             idx = i
#             idx_data += [idx]
#     for i in range(len(max_data)-1):
#         if max_data[i] == max_data[i+1]:
#             result = 0
#     if result ==0:
#         print(f'#{a} {data[idx_data[-1]]} {max}')
#     else:
#         print(f'#{a} {data[idx]} {max}')

# T = int(input())
#
# for a in range(1,T+1):
#     N = int(input())
#     ai = input()
#     data = [0]*10
#     for i in range(10):
#         for j in range(N):
#             if i == int(ai[j]):
#                 data[i] += 1
#     max=0
#     idx=0
#     for i in range(10):
#         if data[i]>=max:
#             max=data[i]
#             idx=i
#     for i in range(10):
#         for j in range(10-i-1):
#             if data[j]>data[j+1]:
#                 data[j],data[j+1] = data[j+1],data[j]
#     print(f'#{a} {idx} {max}')
#9차시 1일차 구간합

T = int(input())

for a in range(1,T+1):
    N , M = map(int,input().split())
    ai = list(map(int,input().split()))
    data=[0]*(N-M+1)
    for i in range(N-M+1):
        for j in range(M):
            data[i] += ai[i+j]

    for i in range(len(data)):
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j] , data[j+1] = data[j+1] , data[j]
    print(f'#{a} {data[-1]-data[0]}')

#민석이의 과제체크하기

T = int(input())

for a in range(1,T+1):
    N , K = map(int,input().split())
    num = list(map(int,input().split()))
    data = [0]*(N+1)
    for i in range(K):
        data[num[i]] = 1
    lst = ''
    ilst = ''
    for i in range(1,N+1):
        if data[i] != 1:
            ilst += ' ' + str(i)
    print(f'#{a}{ilst}')