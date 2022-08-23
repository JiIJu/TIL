# 카드게임 분할정복 함수
# i,j : i번째 학생부터 j번째 학생까지

def tournament(i,j):
    if i == j:
        #i랑j가 같으면 둘로 쪼개는게 불가능
        return i

    #오른쪽과 왼쪽을 나누는 일을 반복적으로 하니 재귀활용
    else:
        left = tournament(i,(i+j)//2)
        right = tournament((i+j)//2 + 1 , j)

        return winner(left,right) # left와 right중 승자를 구해서 리턴

#왼쪽과 오른쪽중에 승자를 정한다.
def winner(left,right):
    if data[left] == 1:
        if data[right] == 1:
            return left
        elif data[right] ==2:
            return right
        elif data[right] ==3:
            return left
    if data[left] == 2:
        if data[right] == 1:
            return left
        elif data[right] ==2:
            return left
        elif data[right] ==3:
            return right
    if data[left] == 3:
        if data[right] == 1:
            return right
        elif data[right] ==2:
            return left
        elif data[right] ==3:
            return left

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = list(map(int,input().split()))


    print(f'#{tc} {tournament(0,(N-1))+1}')

