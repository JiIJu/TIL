# 반댓말 을 만들어주는 함수를 작성해보자.

# correct : 정확한 => in 을 붙여서 반댓말을 만든다.
# incorrect : 부정확한

# 아래의 경우에는 in 이 아니라 변화형이 앞에 붙게 된다.
# 1. 단어가 b 또는 m 또는 p 로 시작하는경우 => im
# 2. 단어가 l 로 시작하는경우 => il
# 3. 단어가 r 로 시작하는경우 => ir

words_dict = {
    "proper": "적절한",
    "possible": "가능한",
    "moral": "도덕적인",
    "patient": "참을성 있는",
    "balance": "균형",
    "perfect": "완벽한",
    "logical": "논리적인",
    "legal": "합법적인",
    "relevant": "관련 있는",
    "responsible": "책임감 있는",
    "regular": "규칙적인",
    "correct": "정확한",
}


def get_opposite(words_dict):  # words_dict 는 반댓말로 바꾸고 싶은 단어들이 들어있다. (딕셔너리로 들어온다.)
    # 반댓말로 만들고 나서 dictionary 형식으로 리턴 할것이기 때문에
    opposite_dict = {}
    # key : 원래단어 / value : 반대 단어
    # { "correct" : "incorrect"}

    for word in words_dict.keys():
        # 반댓말로 만들때 원래 단어가 어떤 철자로 시작하는지를 알아야 규칙을 적용할수 있다.
        start = word[0]
        # 리턴할 반대의미를 가진 단어
        opposite = ""
        # 조건문을 통해서 start가 어떤 철자인지 알아본 후에 규칙을 적용
        opposite_list = []
        if start == "b" or start == "m" or start == "p":
            opposite = "im" + word
        elif start == "l":
            opposite = "il" + word
        elif start == "r":
            opposite = "ir" + word
        else:
            opposite = "in" + word

        # 반댓말을 만들고 나서 딕셔너리에 추가를 해준다.
        opposite_dict[word] = opposite  # word 키에 opposite value(값)를 짝지어 준다.
        opposite_list.append(opposite)

    sorted_list = sorted(opposite_list)  # 반댓말만 들어간 리스트가 정렬이 된다.
    sorted_result = sorted(opposite_dict.items(), key=lambda item: item[1])
    # 원래밀 : 반댓말 이렇게 이루어진 딕셔너리에서
    # items() => (key , value)
    # item = (key, value)
    # item[0] key
    # item[1] value <== 요걸 기준으로 정렬하겠다.
    # 반댓말(value) 를 기준으로 정렬할때
    return sorted_result


print(get_opposite(words_dict))
