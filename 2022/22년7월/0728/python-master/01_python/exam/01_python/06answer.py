# 시저 암호화 방식 프로그램(함수) 만들기

# n만큼 문자를 밀어서 치환한다
# A 를 3번 밀었다 ==> A => B => C => D 결과 : D
# ABC 를 3번 밀었다. ==> DEF

# 암호화할 문자열과, 몇만큼 밀어야하는지?
# word             , n

string1 = "apple"
string2 = "ssafy"


def caesar(word, n):
    # 1. 문자열을 리스트로 바꿔서 해결하기
    str1 = list(word)  # 문자열을 리스트로 바꾼후 저장
    # "apple" => ['a','p','p','l','e']
    # 아스키 코드를 이용해서 암호화

    # 반복문을 사용해서 리스트 안에있는 알파벳이 대문자인지 소문자인지를 판별
    for i in range(len(str1)):
        # i가 대문자인지? 소문자인지?
        if str1[i].isupper():  # 대문자이다.
            # 대문자일 경우 아스키코드의 범위 65 ~ 65 + 26
            # 암호화를 여기서
            # A : 65 를 3번 밀었다.
            # D : 65 + 3
            # str[i] = str(ord(str[i]) + n)
            # Z 일경우 문제가 발생한다
            # 그냥 n 만 더할 경우 아스키코드의 범위를 벗어나기 때문에
            # 벗어난 만큼 다시 알파벳의 처음 아스키 코드로 돌아와서
            # 더해주는 처리가 필요하다.
            # 일단 다 더한다음에 알파벳의 처음 시작지점으로부터
            # 얼마나 떨어져 있는지 확인한 다음에
            # 알파벳의 개수인 26 으로 나눈 다음 그 나머지만큼 더해준다.
            # 다시 알파벳의 시작지점 아스키코드를 더해서 결과를 얻는다.
            str1[i] = chr((ord(str1[i]) + n - 65) % 26 + 65)
        elif str1[i].islower():  #  소문자이다.
            # 소문자일 경우 아키코드의 범위 97 ~ 97 + 26
            # 소문자 a부터 얼마나 떨어져있는지를 구한 다음
            # 소문자 a에 해당하는 코드 + 떨어져 있는 만큼의 수
            str1[i] = chr((ord(str1[i]) + n - 97) % 26 + 97)
    return "".join(str1)

    # 2. 문자열을 그대로 사용해서 해결하기
    result = ""  # 암호화할 문자열을 저장할 변수
    for char in word:  # word 를 리스트로 바꾸지 않고 쓰기
        # 대문자일 경우
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            char = chr((ord(char) + n - 65) % 26 + 65)
        # 소문자일 경우
        elif char in "abcdefghijklmnopqrstuvwxyz":
            char = chr((ord(char) + n - 97) % 26 + 97)
        result += char  # 바꾼 결과를 result에 저장

    return result


print(caesar("apple", 5))
print(caesar("ssafy", 1))
print(caesar("Python", 10))
