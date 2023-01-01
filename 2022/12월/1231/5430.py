# 5430 AC
from collections import deque

T = int(input())

for tc in range(T):
    # R: 배열순서 뒤집기 D: 첫번째수 버리기(배열비었는데 쓰면 에러)
    p = input()
    n = int(input())
    data = input()
    data = data[1:len(data)-1].split(',')
    ans = deque()
    for i in data:
        if i:
            ans.append(i)
    temp=0
    cnt=0
    for i in p:
        if i=='R':
            cnt+=1
        elif i=='D':
            if ans:
                if cnt%2:
                    ans.pop()
                else:
                    ans.popleft()
            else:
                print('error')
                temp=1
                break

    if temp==0:
        if ans:
            if cnt%2:
                ans.reverse()
                print('[', end='')
                for i in range(len(ans) - 1):
                    print(ans[i], end=',')
                print(f'{ans[-1]}]')
            else:
                print('[',end='')
                for i in range(len(ans)-1):
                    print(ans[i],end=',')
                print(f'{ans[-1]}]')
        else:
            print('[]')
