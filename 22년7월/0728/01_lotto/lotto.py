# 여기에 필요한 모듈을 추가합니다.
import random
import json

class Lotto:
    # 2-2. 생성자 작성
    def __init__(self):
        #빈 리스트를 인스턴스변수인 number_lines에 할당한다.
        self.number_lines = []


    # 2-3. n 줄의 로또 번호를 생성하는 인스턴스 메서드
    def generate_lines(self, n):
        #로또 당첨 번호를 n줄 생성해서 인스턴스 변수인 number_lines에 추가
        for i in range(n):
            # 1부터 45까지의 수 중에서 중복없이 6개 뽑기 + 정렬
            line = sorted(random.sample(range(1,46),6))
            self.number_lines.append(line)
            
        # self.n = n
        # num = []
        # for i in range(1,46):
        #     num.append(i)
        # for i in range(n):
        #     result = set()
        #     while len(result)<6:
        #         # result = [random.choice(num) for _ in range(6)]
        #         result.add(random.choice(num))
        #     result = list(result)
        #     result.sort()
        #     self.number_lines.append(result)     
    # 3-3. 해당 회차 추첨일의 년, 월, 일 정보를 튜플로 반환하는 스태틱 메서드
    # 3-2. 회차, 추첨일, 로또 번호 정보를 출력하는 인스턴스 메서드
    def print_number_lines(self, draw_number):
        year = Lotto.get_draw_date(draw_number)
        month = Lotto.get_draw_date(draw_number)
        day = Lotto.get_draw_date(draw_number)

        print ('==================================')
        print(f'            제{draw_number}회 로또')
        print ('==================================')
        print(f'추첨일 : {year}/{month}/{day} (토)')
        print ('==================================')

        #아스키 코드를 이용해서 A~E로 줄번호 출력
        #A는 아스키 숫자로 65 B는 66 E는 69
        for i,line in enumerate(self.number_lines):
            print(f'{chr(65+i)} : {line}')

        # a = Lotto.get_draw_date(draw_number)

        # print('=========================================')
        # print(f'           제 {draw_number}회 로또        ')
        # print('=========================================')
        # print(f'추첨일 : {a[0]}/{a[1]}/{a[2]} (토)')
        # print('=======================================')
        # eng = ['A','B','C','D','E']
        # for i in range(self.n):
        #     print(f'{eng[i]} : {self.number_lines[i]}')

    

    # 4-2. 해당 회차의 당첨 번호와 당첨 결과를 출력하는 인스턴스 메서드
    def print_result(self, draw_number):
        #메인번호 , 보너스번호를 추출해서 가져오기
        main_numbers , bonus_number = Lotto.get_lotto_numbers(draw_number)

        print('====================================')
        print(f'당첨번호 : {main_numbers} + {bonus_number}')
        print('====================================')

        for i , line in enumerate(self.number_lines):
            # 우리가 뽑은 번호와 당첨 번호를 비교
            # 일치하는 갯수 , 보너스 번호 일치 여부
            same_name_counts , is_bonus = Lotto.get_same_info(main_numbers, bonus_number, line)
        ranking = Lotto.get_ranking(same_main_counts, is_bonus)

        #각 로또 번호 줄에 대해서 당첨 결과를 출력
        result = f'{chr(65+i) : {same_name_counts}개}'
        if is_bonus:
            result += ' + 보너스'
        result += '일치'
        result += '낙첨' if ranking == -1 else f'{ranking}등 당첨'
        print(result)
        # c = Lotto.get_lotto_numbers(draw_number)

        # print('=======================================')
        # print(f'당첨 번호 : {c[0]} + {c[1]}')
        # print('=======================================')
 
        # d = Lotto.get_same_info(c[0], c[1], self.number_lines)

        # for i in range(self.n):
        #     for j in range(7):


    # # 3-3. 해당 회차 추첨일의 년, 월, 일 정보를 튜플로 반환하는 스태틱 메서드
    @staticmethod
    def get_draw_date(draw_number):
       lotto_json = open(f'data/lotto_{draw_number}.json')
       lotto_dict = json.load(lotto_json)
       draw_date = lotto_dict.get('drwNoDate') #추첨날짜정보 추출
       year , month , day = draw_date.split('-')

        # file1 = open(f"data/lotto_{draw_number}.json")
        # dict1 = json.load(file1)
        # date = dict1.get('drwNoDate').split('-')
        # year = date[0]
        # month = date[1]
        # day = date[2]
        # return year , month , day
        # return year, month, day

    # 4-3. 해당 회차 당첨 번호의 메인 번호와 보너스 번호가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_lotto_numbers(draw_number):
        lotto_json = open(f"data/lotto_{draw_number}.json")
        lotto_dict = json.load(lotto_json)
        
        
        main_numbers = sorted([value for key,value in lotto_dict.items() if key.startswith('drwt')])

        bonus_number = lotto_dict.get('bnusNo')
        
        return main_numbers, bonus_number

        # for i in range(1,7):
        #     main_numbers.append(lotto_dict.get(f'drwtNo{i}'))
        # main_numbers.sort()
        # bonus_number = dict1.get('bnusNo')

        # return main_numbers, bonus_number

    # 4-4. 한 줄의 로또 번호와 메인 번호가 일치하는 개수와 보너스 번호 일치 여부가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_same_info(main_numbers, bonus_number, line):
        #한줄의 로또 번호와 메인 번호를 비교해서 몇개가 일치하는지
        same_main_counts = 0

        #집합을 사용해서 겹치는 번호의 개수 알아내기
        same_main_counts =  len(set(main_numbers) & set(line))

        # 보너스 번호가 일치하는지
        is_bonus = True

        if bonus_number in line:
            is_bonus == True
        else:
            is_bonus == False

        # for i in range(len(line)):
        #     count = 0
        #     bonus = 0
        #     same_main_counts = []
        #     is_bonus = []
        #     for j in range(6):
        #         for k in range(6):
        #             if main_numbers[j] == line[i][k]:
        #                 count +=1
        #         same_main_counts.append(count)    
        #     for j in range(6):
        #         if bonus_number == line[i][j]:
        #             bonus = True
        #         else:
        #             bonus = False
        #         is_bonus.append(bonus)
            
        return same_main_counts, is_bonus

    # 4-5. 당첨 결과를 정수로 반환하는 스태틱 메서드
    @staticmethod
    def get_ranking(same_main_counts, is_bonus):
        ranking = -1 #등수가 없을 때 -1

        if same_main_counts == 6:
            ranking = 1
        elif same_main_counts==5:
            ranking ==2 if is_bonus==True else ranking ==3
        elif same_main_counts == 4:
            ranking ==4
        elif same_main_counts == 3:
            ranking ==3 
        else:
            ranking = -1

        return ranking
l1 = Lotto()
l1.generate_lines(5)
l1.get_draw_date(1023)

l1.print_number_lines(1023)
l1.print_result(1023)
