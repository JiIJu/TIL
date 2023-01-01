# 부분집합 비트연산자

# arr = [-6,6,7,1,5,4]
#
# n = len(arr)
# result = 0
# data = [[] for _ in range(1<<n)]
# for i in range(1<<n): #1<<n : 부분집합의 개수
#     for j in range(n): # 원소의 수만큼 비트를 비교함
#         if i & (1<<j): #i의 j번 비트가 1인경우
#             data[i].append(arr[j])
#
# for i in range(1<<n):
#     if sum(data[i]) == 0:
#         result = 1
# print(result)

# 문자열 뒤집기
#
# word = 'reverse this strings'
# word_len = len(word)
# a = ''
# for i in range(word_len-1,-1,-1):
#     a += word[i]
# print(a)

# Brute Force

# def BruteForce(a,b):
#     i = 0 #긴문자열 인덱스
#     j = 0 #찾을 문자열 인덱스
#     M = len(b) #찾을 문자의 길이
#     N = len(a) #긴 문자의 길이
#     while j<M and i<N:
#         if a[i] != b[j]:
#             i = i-j
#             j = -1
#         i +=1
#         j +=1
#     if j == M:
#         return i-M # 시작 인덱스 리턴
#     else:
#         return -1 #찾기실패

# push 알고리즘

def push(item):
    s.append(item)

# 괄호검사
#
# text = input()
#
# text_len = len(text)
# stack = []
# result = 1
# for i in range(text_len):
#     if text[i]=='(':
#         stack.append(text[i])
#     elif text[i] == ')':
#         if len(stack) == 0:
#             result = 0
#             break
#         stack.pop()
# if len(stack)>0:
#     result = 0
# print(result)

# 비밀번호
#
# for tc in range(1,11):
#     N , data = input().split()
#     N = int(N)
#     stack = []
#
#     for i in data:
#         if len(stack) == 0:
#             stack.append(i)
#         elif stack[-1] == i:
#             stack.pop()
#         else:
#             stack.append(i)
#
#     print(f'#{tc}',end=' ')
#     for i in stack:
#         print(i,end='')
#     print()

T = int(input())

for tc in range(1,T+1):
    data = [list(map(int,input().split())) for _ in range(9)]
    result = 1

    for i in range(9):
        num = [0] * 10
        for j in range(9):
            num[data[i][j]] =1

        for j in range(1,10):
            if num[j] !=1:
                result = 0
                break
    for i in range(9):
        num = [0] * 10
        for j in range(9):
            num[data[j][i]] = 1

        for j in range(1, 10):
            if num[j] != 1:
                result = 0
                break

    for i in range(0,9,3):
        for j in range(0,9,3):
            num = [0] * 10
            for k in range(3):
                for l in range(3):
                    num[data[i+k][j+l]] = 1
            for j in range(1, 10):
                if num[j] != 1:
                    result = 0
                    break
    print(f'#{tc} {result}')