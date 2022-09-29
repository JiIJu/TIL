

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    data = list(map(int,input().split()))
    temp = [0]*N
    temp[M] = 'goal' # 목표값을 골라서 미리 값을 바꿔놓는다.


    cnt = 0
    while True:
        if data[0] == max(data): # 첫번째 값이 데이터에서 가장 크면 cnt +1
            cnt+=1
            if temp[0]=='goal': # 첫번째 temp가 goal이면 답 프린트
                print(cnt)
                break
            else:
                data.pop(0)     # goal이 아니면 pop
                temp.pop(0)
        else:
            data.append(data.pop(0))
            temp.append(temp.pop(0))


