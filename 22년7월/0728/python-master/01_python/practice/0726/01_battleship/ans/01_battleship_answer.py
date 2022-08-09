import random  # 랜덤 모듈 활용

print("================================")
print("        Battle Ship Game        ")
print("            START !!            ")
print("================================")

# 필요에 따라 추가적으로 함수를 만들어 자유롭게 활용할 수 있습니다.
# 각자의 해역에 배를 위치시키는 함수
def set_ship(index, sea):
    # index : 배의 시작 위치
    # sea : 해역 정보, 배가 있는 위치는 1로 표시하고, 나머지는 0
    # index 로부터 (포함) 3칸에 배를 위치시킨다.
    for i in range(3):  # i = 0, 1, 2
        sea[index - 1 + i] = 1


player_sea = [0] * 15  # 플레이어의 해역
player_attacked = [False] * 15  # 플레이어의 공격 위치 기록

computer_sea = [0] * 15  # 컴퓨터의 해역
computer_attacked = [False] * 15  # 컴퓨터의 공격 위치 기록

round = 1  # 게임 라운드

# 1. 게임 준비
while True:
    # 1-1) 플레이어의 배 시작 위치 고르기
    player_index = int(input("배를 위치시킬 시작점을 고르세요. : "))

    # 반복을 통해 입력을 계속 받는데... 언제까지 입력받을거냐?
    # break 라는 키워드를 통해 꼭 반복을 종료시켜줘야 한다.
    # 플레이어가 제대로 된 배의 위치를 입력할 때까지 반복한다. => 제대로 된 위치를 입력하면 반복 종료
    # 해역의 범위는 1~15 , 플레이어는 배의 첫부분의 위치를 입력한다. 배는 길이가 3칸
    if 1 <= player_index <= 13:
        break

    # 1-2) 범위를 벗어난 시작점을 고른 경우
    print()
    print("----해당 위치에는 배를 놓을 수 없습니다.----")


# 1-3) 컴퓨터의 배 시작 위치를 랜덤으로 지정합니다.
computer_index = random.randint(1, 13)

# 1-4) 플레이어와 컴퓨터의 해역에 각각 배 위치시키기
set_ship(player_index, player_sea)
set_ship(computer_index, computer_sea)


# 2. 라운드 진행
while True:
    # 2-1) 플레이어 공격
    print("--------------------------------------------")
    print("< Information Board >")
    print("플레이어의 해역 : ", player_sea)
    print("플레이어의 공격 기록 : ", player_attacked)
    print("--------------------------------------------")
    print()

    # 2-2) 플레이어의 공격 위치 선택
    player_attack_index = int(input("공격할 위치를 선택하세요 : "))
    print()

    # 플레이어가 입력한 위치가 제대로 된 위치인지 검사

    # 1. 입력한 위치가 해역의 범위를 벗어난경우
    if player_attack_index < 1 or player_attack_index > 15:
        print("해역의 범위에서 벗어난 위치를 선택하셨습니다. 다시 선택해주세요.")
        continue

    # 2. 입력한 위치가 전에 공격한 적이 있는 위치인 경우
    if player_attacked[player_attack_index - 1]:
        print("이미 공격한 위치를 선택하셨습니다. 다시 선택해 주세요.")
        continue
    # ==> 다시 돌아가서 입력을 받아야한다. : continue

    # 여기 있는 코드가 실행 되었다 ==> 플레이어가 위치를 잘 입력했다.

    print(f"<{round}라운드 결과!>")

    # 2-3) 플레이어의 공격이 성공한 경우
    # 플레이어의 공격이 성공했다 ??
    # 컴퓨터 해역의 정보와 플레이어가 입력한 공격 위치를 비교
    # 플레이어가 입력한 공격위치에 컴퓨터 배가 있다면 공격 성공
    # 컴퓨터 해역정보 리스트의 플레이어가 입력한 공격 위치에 있는 데이터를 확인해서 그 값이 1이면 공격 성공!!
    if computer_sea[player_attack_index - 1] == 1:
        print(f"컴퓨터의 해역 : {computer_sea}")
        print(f"플레이어는 컴퓨터의 해역 {player_attack_index}번째 칸을 공격했습니다. 컴퓨터의 배는 피격되었습니다.")
        print(f"게임이 종료되었습니다!! {round}라운드 만에 플레이어가 승리하였습니다.")
        break

    # 2-4) 플레이어의 공격이 실패한 경우
    # 플레이어가 공격한 위치를 기록합니다.
    player_attacked[player_attack_index - 1] = True
    print(f"플레이어는 컴퓨터의 해역 {player_attack_index}번째 칸을 공격하였으나, 공격에 실패하였습니다.")

    # 2-5) 컴퓨터의 공격 위치 지정
    # 컴퓨터가 공격하지 않은 위치를 나타내는 리스트
    computer_attack_range = []

    # 컴퓨터가 공격한 적이 없는 위치만 골라서 위의 리스트에 넣어준다.
    # computer_attacked를 모두 검사하면서 값이 False 인 위치만 골라서 넣어준다.
    for i in range(len(computer_attacked)):  # i는 computer_attacked 리스트의 인덱스
        if not computer_attacked[i]:  # 컴퓨터가 공격한적이 없는 위치이다!
            computer_attack_range.append(i + 1)

    computer_attack_range = [
        i + 1 for i in range(len(computer_attacked)) if not computer_attacked[i]
    ]
    computer_attack_range = [
        i + 1 for i, log in enumerate(computer_attacked) if not log
    ]  # log 는 i+1 번째 위치의 공격한 적이 있는지 나타내는 boolean 값 == computer_attacked[i] == log

    computer_attack_index = random.choice(
        computer_attack_range
    )  # 컴퓨터가 공격 가능한 위치 랜덤 고르기

    # 2-6) 컴퓨터의 공격이 성공한 경우
    if player_sea[computer_attack_index - 1] == 1:
        print(f"컴퓨터가 플레이어의 해역 {computer_attack_index}번째 칸을 공격하였습니다. 플레이어의 배는 피격되었습니다.")
        print(f"게임이 종료되었습니다!! {round}라운드 만에 컴퓨터가 승리하였습니다.!!")
        break

    # 2-7) 컴퓨터의 공격이 실패한 경우
    computer_attacked[computer_attack_index - 1] = True  # 컴퓨터가 공격한 위치 저장
    print(f"컴퓨터는 플레이어의 해역 {computer_attack_index}번째 칸을 공격했으나, 공격에 실패하였습니다.!")
    print()

    # 여기까지 오면 (반복문이 끝나지 않았다면) 둘다 공격에 실패했다 라는 의미이므로
    # 다음라운드로 진행해준다.
    round += 1
