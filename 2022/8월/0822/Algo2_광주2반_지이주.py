T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)] #2차원배열
    pat = [list(map(int,input().split())) for _ in range(3)] #패턴 입력
    ans = []
    for i in range(N-2):  #ans라는 빈 배열에 2차원 배열의 값을 모두 넣는다.
        for j in range(N-2):
            for k in range(3):
                for l in range(3):
                    ans += [data[i+k][j+l]]
    new = []
    count = 0
    for i in range(3): #new라는 배열에 2차원배열로 받은 패턴을 1차원배열로 나열한다.
        for j in range(3):
            new += [pat[i][j]]
    n = (N-2)*(N-2)*9 # 패턴을 확인하는 총 경우의 수
    result = 0
    for i in range(0,n,9): # 1차원으로 나열된 패턴과 N*N배열의 값을 비교하며 값이 같다면 result값을 1 더한다.
        count = 0
        for j in range(9):
            if ans[i+j]==new[j]:
                count+=1
            if count ==9:
                result +=1
    print(f'#{tc} {result}')
