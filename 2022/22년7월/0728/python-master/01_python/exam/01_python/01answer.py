# 리스트가 주어질때, 그 리스트 안에있는 원소들의 총 합 구하기
def total(scores):  # scores : 시험점수가 들어있는 리스트
    # 반복문 사용
    result = 0  # 시험점수의 총합을 저장할 변수
    for score in scores:
        result += score
    return result

    # sum() 함수 사용
    return sum(scores)
