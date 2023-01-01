# 봉우리 : 높아지다가 낮아지는 지형
# 맨앞 : 다음지형보다 높으면 , 맨뒤 : 앞지형보다 높으면

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    # 맨앞과 맨 뒤의 케이스를 처리해주기 위해 양 끝값에 0을 추가
    data = [0]+list(map(int,input().split()))+[0]


    cnt = 0
    n = 0
    # 앞의 높이보다 크고 뒤의 높이보다 작으면 봉우리이므로 그 때 cnt를 1 올려줌
    # 최고높이가 같은 경우도 있으므로 등호표시
    for i in range(N):
        if data[i]<=data[i+1] and data[i+2]<data[i+1]:
            cnt+=1
    print(f'#{tc} {cnt}')