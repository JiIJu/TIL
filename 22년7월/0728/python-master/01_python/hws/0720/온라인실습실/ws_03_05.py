salt = 0  # 소금의 양
water = 0  # 소금물의 양

count = 0  # 현재 내가 입력한 소금물의 갯수
while count < 5:
    command = input("농도 입력(Done 입력시 종료) : ")
    if command == "Done":
        break  # 반복문을 즉시 종료

    # 여기는 Done 을 입력하지 않았다 ==> command에 농도가 들어있다.
    density = int(command)  # 농도
    brine = int(input("소금물 입력 : "))  # 소금물

    # 지금까지 입력받은 소금물의 소금양을 누적시킨다.
    salt += density * brine
    # 지금까지 입력받은 소금물의 총합
    water += brine

    # 입력 하나 받았으니까 count 증가
    count += 1

# 혼합물의 농도와 총양을 출력해달라!!
# .2f ==> 소수점 2번째 자리까지 출력해주세요
print(f"혼합물의 농도는{salt/water}% , 양은{water} 입니다.")
salt /= 100
density = salt / water
print("혼합물의 농도는{:.2f} , 양은{}".format(density, water))
