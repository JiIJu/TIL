#cnt : 카드를 교환한 횟수
def card_swap(cnt):
    global max_val

    # 중단조건
    #교환횟수를 다 썼으면 그 때 최대상금을 구하면 된다.
    if cnt == N:
        num = int(''.join(S))
        max_val = max(max_val,num)
        return # 함수를 종료

    # 부분문제
    # 교환횟수가 남았으면 카드를 바꾼다.
    #교환시작위치  i , 교환대상위치 j
    for i in range(len(S)-1):
        for j in range(i+1,len(S)):
            # i위치 카드와 j위치 카드교환
            S[i] , S[j] = S[j] , S[i]
            #교환한 상태로 다음 교환으로 넘어가기
            card_swap(cnt+1)
            #계산했으면 교환전의 상태로 되돌린다.
            S[j] , S[i] = S[i] , S[j]



T = int(input())

for tc in range(1,T+1):

    S,N = input().split()

    S = list(S)
    N = int(N)


    #똑같은 자리에서 교환중복을 허용한다 했지만 결국 우리가 해당 자리수로 만들수있는 숫자는
   # 해당자리수만큼 교환을 실행한 결과와 같을것이다. 주어진 교환횟수가 카드의수보다 커지면
   # 의미가 없어진다. 그경우 교환횟수를카드의수로제한힌디

    if N>len(S):
        N = len(S)
