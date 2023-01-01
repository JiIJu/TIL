def ThirtyOne(month):
    print(31 , 'days for',year,'-',(int(month)))

def Thirty(month):
    print(30 , 'days for',year,'-',(int(month)))

def TwentyEight(month):
    if year%4==0 and (year%100 !=0 or year%400 ==0):
        print(29 , 'days for',year,'-',(int(month)))
    else:
        print(28 , 'days for',year,'-',(int(month)))

year = int(input())
month = input()

dic = {'1':ThirtyOne,'3':ThirtyOne,'5':ThirtyOne,'6':ThirtyOne,'8':ThirtyOne,'10':ThirtyOne,'12':ThirtyOne,'4':Thirty,'6':Thirty,'9':Thirty,'11':Thirty,'2':TwentyEight}

func = dic.get(month)

func(month)