# 비밀번호의 길이가 8 이상 32 이하 인지 검사하는 함수


def check_password_length(password):  # password : 비밀번호에 해당하는 문자열
    return 7 < len(password) < 33


password = "1q2w3e4r"

print(check_password_length(password))
