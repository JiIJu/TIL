# test1 = '()()((()))'
# test2 = '((()((((())((()())((())))))'
#
# data = input()
#
# stack = []
# result = 0
# for i in data:
#     if i == '(':
#         stack.append(i)
#     elif i == ')':
#         if len(stack)==0:
#             result = -1
#         elif stack.pop() != '(':
#             result = -1
#
# if stack:
#     result = -1
#
# print(result)
# s : start
# V : 정점의 개수
# 0 1 2 3 4 5 6 7
adj = [[0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 0, 0, 0, 0],  # A
       [0, 1, 0, 0, 1, 1, 0, 0],  # B
       [0, 1, 0, 0, 0, 1, 0, 0],  # C
       [0, 0, 1, 0, 0, 0, 1, 0],  # D
       [0, 0, 1, 1, 0, 0, 1, 0],  # E
       [0, 0, 0, 0, 1, 1, 0, 1],  # F
       [0, 0, 0, 0, 0, 0, 1, 0]]  # G

def dfs(s,V):
    # 정점의 방문여부를 알기 위한 배열 선언
    visited = [0] * (V+1) # 0번 인덱스는 사용안함
    stack = [] # size는 생각안함
    now = s # 현재 위치는 now로 표현
    visited[now] = 1 # 시작 위치는 방문했다고 체크
    print(now,end=' ')
    # while len(stack)!=0
    while True: # 현재 위치가 0이 아닐때 까지 ( 시작 위치로 돌아오지 않을때 까지 반복)
        # 다음 방문 위치를 방문
        for w in range(1,V+1): # 1부터 V번 정점 방문하기
            # 다음 방문 위치 처리
            if adj[now][w] ==1 and visited[w] == 0:
            # 현재 위치를 스택에 저장
                stack.append(now)
            # 다음 방문 위치를 방문했다고 체크
                visited[w] = 1
                print(w, end=' ')
            # 현재 위치를 다음 위치로 바꾸고
                now = w
            # 탈출
                break
        else:
            # 다음 방문 위치가 없다 (방문한곳만 남거나 아니면 인접한곳이 없다.)
            if stack: # 스택이 비어있지 않으면 아직 방문할 곳이 남았다.
                # 지난 정점으로 돌아가기
                now = stack.pop()
            else:   # 스택이 비어있다. => 탐색중지
                # 무한루프 중지
                break
    return


dfs(1,7)
