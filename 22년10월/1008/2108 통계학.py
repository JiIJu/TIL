def find(li):   # 최빈값 처리를 위한 함수 같은수의 최빈값이 있으면 2번째 큰값 리턴
    num = [0]*8001  # -4000~4000 처리를 위해 리스트생성
    for s in li:
        ss = s+4000
        num[ss]+=1
    max_num = max(num)
    max_index = num.index(max_num)
    if num.count(max_num)>1:
        num[max_index] = 0
    return num.index(max_num) - 4000
N = int(input())
data = []
for i in range(N):
    data.append(int(input()))
if sum(data)>0:
    print(int(sum(data)/N+0.5))
else:
    print(int(sum(data) / N-0.5))
sort_data = sorted(data)
print(sort_data[N//2])
print(find(data))
print(max(data)-min(data))