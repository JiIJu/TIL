# N = int(input())    # 처음풀이 ==> 시간초과
# data = [0]*N
# for i in range(N):
#     data[i]=i+1
# stack=[]
# while len(data)>1: # 제일처음값 없애고 그다음 앞에값을 뒤에 추가
#     data.pop(0)
#     stack.append(data.pop(0))
#     data.append(stack[-1])
# print(data[0])

a = int(input())
b = 2
while True: # 규칙을 찾아서 해결
    if a == 1 or a == 2:
        print(a)
        break
    b *= 2
    if b >= a:
        print((a - (b // 2)) * 2)
        break