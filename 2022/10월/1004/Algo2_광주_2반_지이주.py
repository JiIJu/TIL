def comb(n): # 조합을 구현하는 함수 작성
    for i in range(1<<n):
        result = []
        for j in range(n):
            if i & (1<<j):
                result.append(a[j])
        ans.append(result)

T = int(input())

for tc in range(1,T+1):
    N , M = map(int,input().split())
    case = [4,6,7,9,11] # 싸피가 수집하는 보석번호
    data = list(map(int,input().split()))
    a = []
    ans = []
    for i in range(N): # 입력된 데이터중 싸피가 수집하는 보석이라면 a에 추가
        for j in range(5):
            if data[i]%case[j]==0:
                a.append(data[i])
                break
    comb(len(a)) # a로 만들수있는 부분집합을 ans에 추가
    maxv = 0
    for i in range(len(ans)): # ans값중 M이하의 값중에 최대값을 구함
        if maxv<sum(ans[i])<=M:
            maxv = sum(ans[i])
    print(f'#{tc} {maxv}')