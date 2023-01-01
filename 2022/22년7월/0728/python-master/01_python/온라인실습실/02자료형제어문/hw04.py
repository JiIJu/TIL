orders = "아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또"

# 각 메뉴가 , 로 구분되어 있으니까 split(",") 써서 리스트로 만들자!!

order_list = orders.split(",")

# 1. 아이스 음료 주문이 몇개 들어왔는지 출력
ice_count = 0  # 아이스 음료 주문 갯수

for drink in order_list:  # order_list를 순회하면서 drink는 계속 바뀐다.
    # in 연산자를 통해 "아이스" 라는 문자열이 drink에 포함되어 있는지를 확인해서 포함되어 있다면 ice_count를 1씩 증가
    if "아이스" in drink:
        ice_count += 1

print(ice_count)


# 2. 각 메뉴당 주문 횟수를 출력
# 아이스 아메리카노 : 2잔
# 라떼 : 3잔
# ....

orders_dict = {}

# 반복문을 통해 음료의 주문횟수를 딕셔너리의 값으로, 음료의 이름을 key로 지정해서 딕셔너리를 수정해나가기
for drink in order_list:
    if orders_dict.get(drink):
        # 값을 가져올수 있다면 조건문이 True
        # { drink : 1 }
        # 1의값을 1증가 시키면 개수를 셀수 있다.
        orders_dict[drink] += 1
    else:
        # 제공한 키에 대한 값을 가져올수 없다면 (해당 딕셔너리에 키가 없다면) False
        # 딕셔너리에 키 : 값 쌍을 추가 해주면 된다!!
        orders_dict.update({drink: 1})

print(orders_dict)
for key, value in orders_dict.items():
    print(f"{key} 는 {value}잔 대기중입니다.")
