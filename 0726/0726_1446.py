def fn_d(n): #n은 입력으로 들어오는 숫자인데, 결과로 각 자릿수를 더하고 , 자기 자신을 더해서 반환
    #91 = 9 + 1 + 91 = 101
    #n을 문자열로 바꿔서 쓰는 방법
    number = str(n)
    # 문자열로 바꾸면 각 인덱스 위치에 있는 철자가 바로 자리수가 된다.
    # 앞에서 부터 하나씩 떼와서 숫자로 다시 바꾼 다음 더해주면 된다.
    
    for i in number: #i는 문자열에서 떼어낸 철자 하나 (숫자로 바꾸면 자릿수)
        n += int(i)
    return n    

number_set = set(range(1,10001)) # 1~10000까지 함수를 이용해서 수를 만든다.
gen_set = set() #함수를 이용해서 만든 수를 저장할 세트
for i in range(1,10001):
    gen_set.add(fn_d(i))
self_set = set() # 셀프넘버를 저장할 세트

self_set = number_set - gen_set #차집합을 이용해서 빼주면 만들 수 없는 숫자들만 남게된다.


print(fn_d(91))

def is_selfnumber(n): 
    #n이라는 수가  selfnumber인가?? => n이라는 숫자가 위에서 만든 fn_d() 함수의 결과로 나올 수 있는 숫자인가?
    #n이라는 숫자가 fn_d()함수를 사용해서 만든 숫자라고 했을 때
    #fn(d)에 입력한 인자(숫자)는 무조건 n보다 작다. 라는 조건을 이용한다.
    #브루트 포스 알고리즘 ==> 모든 경우의 수를 시도해서 문제를 해결하는 알고리즘
    # for number in range(1,n+1):
    #     if fn_d(number) == n: #함수를 통해 만들수 있는 숫자다? ==> 셀프넘버가 아니다.
    #         return False
    #     return True # 반복문이 끝나면 함수를 통해 만들 수 없는 숫자다 ==> 셀프넘버다.
    return n in self_set


print(is_selfnumber(33))