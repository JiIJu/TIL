# data = input()

# if len(data)%2 != 0:
#     print(data[int((len(data)-1)/2)])
# else:
#     print(data[int(len(data)/2-1):int(len(data)/2)+1])

# def get_middle_char(a):
#     if len(a)%2 != 0:
#         print(a[(len[a]-1)/2])
#     else:
#         print(a[int((len(a)/2)-1):int(len(a)/2)+1])
# word = input()
# get_middle_char(word)

# s_triangle = input().split()
# s_triangle.sort()
# print(s_triangle)
# if (int(s_triangle[0])+int(s_triangle[1]))  > int(s_triangle[2]):
#     if int(s_triangle[0]) == int(s_triangle[1]) == int(s_triangle[2]):
#         print("정삼각형")
#     elif (int(s_triangle[0])==int(s_triangle[1])!=int(s_triangle[2]) or int(s_triangle[0])==int(s_triangle[2])!=int(s_triangle[1]) or int(s_triangle[0])!=int(s_triangle[1])==int(s_triangle[2])):
#         print("이등변 삼각형")
#     elif int(s_triangle[2])**2 == int(s_triangle[0])**2 + int(s_triangle[1])**2:
#         print("직각 삼각형")
#     else:
#         print("삼각형")
    
# else:
#     print("삼각형이 아니다.")        

# numbers = [
#     85 , 72 , 38 , 80 , 69 , 65 , 68 , 96 , 22 , 49 , 67 ,
#     51 , 61 , 63 , 87 , 66 , 24 , 80 , 83 , 71 , 60 , 64 ,
#     52 , 90 , 60 , 49 , 31 , 23 , 99 , 94 , 11 , 25 , 24 
# ]

# numbers.sort()

# if len(numbers)%2 == 0:
#     print(numbers[(int(len(numbers)/2))])
# else:
    
#     print(numbers[int((len(numbers)-1)/2)])


#데일리실습 1680

# fruits = "apple,rottenBanana,apple,RoTTenorange,orange"
# fruit_list = fruits.split(",")
# fresh_list = []
# #반복문을 사용해서 리스트 안의 썩은 과일을 새거로 만든다음 신선한 과일주머니로 옮긴다
# #썩은 과일이 아닐경우 신선한 과일 주머니로 그대로 옮겨도 된다

# for fruit in fruit_list:
#     if "rotten" in fruit.lower():
#         #썩은과일이다 ==> 신선한 과일로 바꿔서 새 주머니로 옮긴다.
#         fresh_list.append(fruit.lower().replace('rotten','')) #replace("바꿀 문자열","변경후 문자열")
#     else:
#         #썩은 과일이 아니다 ==> 그대로 새 주머니에 옮겨준다.
#         fresh_list.append(fruit.lower())

# print(fresh_list)

#데일리실습 1681
# str1 = input()
# result = ""

# length = len(str1)
#문자열의 길이가 짝수인가? 홀수인가?
# if length % 2 == 0: #짝수인 경우 가운대 2개 문자
#     result = str1[(length//2)-1] + str1[(length//2)]
# else:
#     result = str[(length//2)]
# print(result)

#데일리실습 1684

#소금물 농도
# salt = 0 #소금의 양
# water = 0 #소금물의 양

# count = 0 #현재 내가 입력한 소금물의 갯수
# while count <5:
#     command = input("농도를 입력하세요(Done 입력시 종료) : ")
#     if command == "Done":
#         break
#     density = int(command)
#     brine = int(input("소금물을 입력 : "))

#     #지금까지 입력받은 소금물의 소금양을 누적시킨다.
#     salt += density * brine
#     water += brine

#     count += 1

# #혼합물의 농도와 총량을 출력해라
# print(f'혼합물의 농도는 {round(salt/water,2)}, 양은 {water}')

# s_triangle = input()
# #map("적용할 함수이름" ,"함수를 적용하고 싶은 리스트")
# t_list = s_triangle.split(",")
# a , b , c = map(int,sorted(t_list))

# if a+b>c:
#     if a==b==c:
#         print("정삼각형")
#     elif a==b or b==c or c==a:
#         print("이등변삼각형")
#     elif c**2==a**2+b**2:
#         print("직각삼각형")
#     else:
#         print("삼각형")
# else:
#     print("삼각형이 아니다.")
# import *
# print(e)

# password = 1111
# n=0
# while n<3:
#     ans = int(input('비밀번호를 입력하세요'))
#     if ans == password:
#         break
#     else:
#         n +=1

students = ['박해피', '이영희', '조민지', '조민지', 
            '김철수', '이영희', '이영희', '김해킹',
            '박해피', '김철수', '한케이', '강디티',
            '조민지', '박해피', '김철수', '이영희',
            '박해피', '김해킹', '박해피', '한케이','강디티']
a = list(set(students))
b = ''
for i in a:
    dict[i] = int(students.count(i))
    
print(dict)
