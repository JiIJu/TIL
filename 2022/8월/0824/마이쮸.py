q = []
n = 10000 # 마이쮸의 개수
m = 0 # 지금까지 나눠준 마이쮸의 개수
p = 1 # 마이쮸를 나눠주기 시작할 사람의 번호
v = 0 # 마지막에 받는 사람이 누군지??

while m<n:
    q.append((p,1,0)) # 마이쮸를 받을 사람을 줄에 세운다 (번호표 주기)
    v,c,my = q.pop(0) # pop() => 맨마지막 원소 / pop(0) => 첫번째원소
    # print(f'큐에 남아있는 사람수 {len(q)-1} 받아갈개수 {c} 나눠준 개수{m}')
    m +=c
    # 마이쮸를 받았으니 다시 받기위해 줄의 맨 뒤로 이동
    q.append((v,c+1,my+c))
    p +=1

print(f'마지막 받은사람 {v}')

q = []
n = 10000
m = 0 # 나눠준 마이쮸 수
p = 1 # 마이쮸 나눠주기 시작할 사람번호
v = 0 # 마지막 받은사람

while n >m:
    q.append((p,1,0))
    v,c,my = q.pop(0)
    m+=c
    q.append((v,c+1,my+c)) # 받아갈 수 c 나눠준 수 my
    p+=1




# from collections import deque
# # deque를 이용해서 구현하기
#
# p=1
# q = deque()
# n = 1000
# m = 0
# v = 0
#
# while m<n:
#     q.append((p,1,0)
#     v,c,my = q.popleft() # 맨 왼쪽원소에서 원소빼기
#     m +=c
#     q.append((v,c+1,my+c))
#     p +=1

