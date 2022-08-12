def get_prime(n):  # n까지의 숫자 중에서 소수를 구한다.
    arr = [True] * (n + 1)  # 일단 n까지의 숫자를 다 소수라고 표시
    arr[1] = False
    m = int(n**0.5)
    for i in range(2, m+1):
        if arr[i]:  # 만약 i번째 수가 소수면
            # 소수의 배수를 모두 소수가 아니라고 체크
            for j in range(i + i, n + 1, i):
                arr[j] = False
    return arr
S = get_prime(1000000)
T = int(input())
for tc in range(1,T+1):
    D, A , B = map(int,input().split())
    count=0
    data = []
    s=0
    for i in range(A,B+1):
        if S[i]:
            i = str(i)
            if str(D) in list(str(i)):
                s += 1
                continue


    print(f'#{tc} {s}')
