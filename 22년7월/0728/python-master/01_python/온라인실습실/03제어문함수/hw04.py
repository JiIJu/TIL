s_triangle = input()  # 입력은 3,4,5 이런식으로 온다고 가정

# , 로 쪼개서 리스트로 만든 후에 오름차순 정렬한다.
a, b, c = map(int, sorted(s_triangle.split(",")))
# sorted(map(int, s_triangle.split(",")))

print(a, b, c)
# 먼저 삼각형인지 아닌지부터 판별한다.
# 오름차순으로 정렬 했으므로 a < b < c 성립
if a + b > c:
    if a == b == c:
        print("정삼각형")
    elif a == b or b == c or c == a:
        print("이등변삼각형")
    elif a**2 + b**2 == c**2:
        print("직각삼각형")
    else:
        print("삼각형")
else:
    print("삼각형이 아니다.")
