#1461
class Nationality:
    def __init__(self,country):
        self.country = country
        print(f'나의 국적은 {self.country}')

korea_nationality = Nationality("대한민국")

#1462
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def details(self,name,age):
        pass

    def check_age(self):
        if self.age>=20:
            return True
        else:
            return False

p1 = Person('이주',1)
print(p1.check_age())

#1463

class PublicTrasport:
    passenger = 0
    total = 0
    def __init__(self,name,fare):
        self.name = name
        self.fare = fare

    def get_in(self,n):
        # self.n = n
        passenger += n
        total += n
        print(f'현재 탑승자 수는 {passenger}명 입니다.')

    def get_off(self,n):
        # self.n = n
        passenger -= n
        total += n
        print(f'현재 탑승자 수는 {passenger}명 입니다.')

    def profit(self):
        return fare * total

p1 = PublicTrasport('이름', 10000)
p1.get_in(5)
p1.get_off(2)
p1.get_in(10)
p1.profit()
