import random
answer = random.randint(1,10000)
counts = 0
is_playing = True
while is_playing == True:
    ans = int(input("1이상 10000이하의 숫자를 입력하세요. :"))
    counts +=1
    if ans <1 or ans>10000:
        print("잘못된 범위의 숫자를 입력하셨습니다. 다시 입력해주세요.")
        continue
    if ans > answer:
        print("down!!!!!")
        continue
    elif ans< answer:
        print("up!!!")
    else:
        print(f'Correct!!! {counts}회 만에 정답을 맞추셨습니다.')
        is_playing = False
        break
