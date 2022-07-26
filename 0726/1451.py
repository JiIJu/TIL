def sum_of_digit(number): #반복문을 활용한 코드
    n = 0
    while number>=10:
        n = n + number%10
        number = number // 10
    return n+number
print(sum_of_digit(105))

def sum_of_digit2(number): #반복문을 사용하지 않는 코드
    if number>=10:
        return number%10 + sum_of_digit2(number//10)
    else:
        return number
print(sum_of_digit2(1054))