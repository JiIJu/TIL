s_triangle = input()  # 입력을 3,4,5 이런식으로 온다고 가정

# split() 함수를 이용해서 , 단위로 문자열을 쪼갠 뒤에 리스트로 만든다.
# 리스트로 만들고 언패킹을 사용해서 3개의 변수에 할당

# map( 적용할 함수 이름, 함수를 적용하고 싶은 리스트 )
# 그 결과는 리스트안에 있는 모든 원소에 함수를 적용시킨다.
t_list = s_triangle.split(",")

a, b, c = map(int, sorted(t_list))
# a < b < c
# a + b > c  ==> 삼각형이 된다.!!!
# 제일 큰변 < 나머지 두변의 합

# 삼각형이 되는지 판단
if a + b > c:
    # 삼각형이다.
    if a == b == c:
        print("정삼각형")
    elif a == b or b == c or c == a:
        print("이등변삼각형")
    elif c**2 == a**2 + b**2:
        print("직각삼각형")
    else:
        print("삼각형")
else:
    print("삼각형이 아니다.")
