# 가운데 문자를 알고싶은 문자열 입력

str1 = input()

result = ""  # 여기에 가운데 문자를 저장
# 입력받은 문자열의 길이가 홀수 ==> 1개
# 입력받은 문자열의 길이가 짝수 ==> 2개

# 문자열의 길이를 이용해서 가운데 위치를 구한다.
# len // 2

# 문자열의 길이
length = len(str1)

# 문자열의 길이가 짝수인가 ? 홀수 인가?
if length % 2 == 0:  # 짝수인 경우 가운데 2개 문자
    result = str1[(length // 2) - 1] + str1[(length // 2)]
else:  # 홀수인 경우 가운데 1개문자
    result = str1[(length // 2)]

print(result)
