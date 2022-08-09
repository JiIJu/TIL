# 어떤 딕셔너리가 있을때, 키를 사용해서 값을 얻어오고,
# 그 값을 비교할수 있는지를 물어보는 문제
def inventory_filter(item_type, inventory):
    # item_type : 내가 알고싶은 아이템의 종류
    # inventory : 전체 아이템목록이 딕셔너리 형태로 들어있다.
    # 아이템은 여러개니까 inventory는 딕셔너리의 리스트가 된다

    result = []  # 내가 알고싶은 아이템만 담을 리스트
    for item in inventory:  # 딕셔너리의 리스트, item : 아이템 하나
        if item.get("type") == item_type:  # 내가 알고싶은 타입과 같다면
            result.append(item)  # 결과 리스트에 하나씩 추가해준다.

    return result

    return [item for item in inventory if item.get("type") == item_type]
