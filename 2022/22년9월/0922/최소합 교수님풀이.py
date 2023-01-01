T = int(input())

for tc in range(1,T+1):

    N = int(input())

    arr  = [list(map(int,input().split())) for _ in range(N)]
    # 중간까지의 합을 다시 계산하지않도록
    # 기억해놓는 방법을 사용한다

    dp = [[0]*N for _ in range(N)]
    # 이동방향이 왼>오 , 위 > 아래
    for i in range(N):
        for j in range(N):
        # 현재 i,j 위치에서 위에서도 올수있고 왼쪽에서도 올수있다면
            if i-1>=0 and j-1>=0:
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+arr[i][j]
            # 위에서만 올수있고 왼쪽에서는 올수없다.
            elif i-1>=0 and j-1<0:
                dp[i][j] = dp[i-1][j] + arr[i][j]
            # 위x왼o
            elif i-1<0 and j-1>=0:
                dp[i][j] = dp[i][j-1] + arr[i][j]
            #왼 x 위 x =>시작점
            elif i-1<0 and j-1<0:
                dp[i][j] = arr[i][j]
    print(dp)