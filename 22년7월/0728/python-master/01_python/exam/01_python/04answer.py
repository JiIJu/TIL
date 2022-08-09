# 현재 회원가입이 되어있는 아이디의 리스트
user_id_list = ["kimssafy", "jungssafy"]
# 회원가입을 목표로 하는 아이디
target_id = "jungssafy"


def check_duplicate_id(target_id, user_id_list):
    # target_id : 회원가입을 목표로 하는 아이디
    # user_id_list : 이미 회원가입이 되어있는 아이디 리스트
    result = target_id in user_id_list
    return result


print(check_duplicate_id(target_id, user_id_list))
