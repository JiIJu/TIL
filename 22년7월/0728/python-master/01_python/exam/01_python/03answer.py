user_data = {"id": "jungssafy", "password": "q1w2e3r4", "password_confirm": "q1w2e3r4"}


def get_user_id(data):  # data안에는 사용자의 정보가 들어있다.
    return data.get("id")
