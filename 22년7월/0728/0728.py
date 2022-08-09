# import random

# class Reset:

#     def __init__(self,name):
#         self.name = name
    
#     def pick(self,name,n):
#         return random.sample(self.name,n)
#     def match_pair(self,name):
#         student = []
#         if len(self.name)%2 == 0 :
#             for i in range(len(self.name)//2):
#                 student.append(random.sample(self.name,2))

# student = Reset(['이진호','강은주','이진후','김은정'])
# print(student.pick(['이진호','강은주''이진후','김은정'],2))
# print(student.match_pair(['이진호','강은주''이진후','김은정']))

from faker import Faker
import random
import copy

class Pairprogramming:
    #1. 인자로 학생들의 이름으로 이루어진 리스트를 받아서 인스턴스 변수에 할당한다.
    def __init__(self,students): #students : 학생들의 리스트
        self.students = students

    def pick(self,n):
        result = set() #결과로 반환할 랜덤으로 뽑은 학생 세트(중복불가)
        while len(result)<n:
            result.add(random.choice(self.students))
        return list(result)
    def match_pair(self):
        result = []
        #학생 리스트를 복사해서(깊은복사)
        #뽑아서 짝을 지어준 학생을 뽑아서 페어링을 해주면 된다.
        #[1,2,3,4,5]
        
        if len(self.students) <2:
            return None

        if len(self.students) % 2 == 1:
        # 학생들의 수가 홀수인 경우 미리 3명을 뽑아서 조를 만들어준다.
            random_pick = self.pick(3)
            # 뽑은 세명은 짝짓기가 완료되었으니까 리스트에서 제거해준다. (다음에 또 뽑지않기위해)
            for student in random_pick:
                self.students.remove(student)
                #결과로 반환할 리스트에 뽑아온 3명 리스트를 추가
            result.append(random_pick)

            #남은 사람이 없을 때 까지 반복한다.
        while len(self.students)>0:
            random_pick = self.pick(2)
            for student in random_pick: #뽑아온 두명은 다음에 뽑지않기위해 제거
                self.students.remove(student)
            result.append(random_pick) #뽑아온 2명을 리스트에 추가
        #반복문이 끝나면 남은 학생이 없다.
        return result
students = []

#학생 리스트 만들기
fake = Faker("ko_KR")

for i in range(11):
    students.append(fake.name())

pair1 = Pairprogramming(students)

print(pair1.pick(6))
print(pair1.match_pair())