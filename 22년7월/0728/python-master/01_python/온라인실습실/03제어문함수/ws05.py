salt = 0
water = 0

count = 0
while count < 5:
    command = input("농도 입력(Done 입력시 종료) :")
    if command == "Done":
        break

    density = int(command)
    brine = int(input("소금물 입력 : "))

    salt += density * brine
    water += brine

    count += 1

print(f"혼합물 농도는{salt/water:.2f}, 양은{water} 입니다.")
