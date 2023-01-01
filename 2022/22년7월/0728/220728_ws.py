#1.pip
#faker을 설치하기위한 명령 , (2) 코드를 작성하기전 제일 위에서 작성

#2. Basic Usages
#1 faker함수에서 faker기능을 꺼내오기위한 코드이다.
#2 faker는 함수 , fake는 변수이다
#3 name()은 fake의 할당값이다.

#3. localization
#(a)init (b) self (c) name

#4. seeding the generator
import random
from faker import Faker
fake1 = Faker('ko_KR')
Faker.seed(87654321)
print(fake1.name()) #이진호
fake2 = Faker('ko_KR')
print(fake2.name()) #강은주

fake1 = Faker('ko_KR')
fake1.seed_instance(87654321)
print(fake1.name()) #이진호
fake2 = Faker('ko_KR')
print(fake2.name()) #강은주