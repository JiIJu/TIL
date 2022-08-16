T = int(input())

for tc in range(1,T+1):
    data = list(input())
    emp = [0] * (len(data))
    count = 0 # ( 의 개수
    laser = 0 #레이저 수
    iron = 0 # 쇠막대기의 수
    cut = 0 #잘린 막대 수
    for i in range(len(data)):  #( 개수와 (가 있는 위치에 1 을 대입 )는 0
        if data[i] == '(':
            count+=1
            emp[i] = 1
    for i in range(len(data)-1):  # 레이저 개수를 구하고 레이저가 있는 위치에 -1대입
        if data[i]=='(' and data[i+1] ==')':
            emp[i] = -1
            emp[i+1] = -1
    zero = 0
    for i in range(len(emp)):
        if emp[i] == 0:
            zero+=1 # )의 개수
    n = 0
    while n<len(emp)-1:
        if emp[n] == -1 and emp[n+1] ==-1:
            cut += iron
            n +=2
            continue
        elif emp[n] == 1:
            iron +=1
            cut += 1
        elif emp[n] == 0:
            iron -=1
        n +=1
    print(f'#{tc} {cut}')
