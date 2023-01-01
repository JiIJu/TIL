# data = [2,4,5,1,3,6]
# a = len(data)
# count = [0] * (a+1)
# arr = [0] * a

# for i in range(a): # 버블정렬
#     for j in range(a-i-1):
#         if data[j]>data[j+1]:
#             data[j] , data[j+1] = data[j+1] , data[j]
# print(data)
# for i in range(a):
#     count[data[i]] +=1
# for i in range(1,a+1):
#     count[i] += count[i-1]
# for i in range(a-1,-1,-1):
#     count[data[i]] -= 1
#
#     arr[count[data[i]]] = data[i]
#
# print(arr)
#


data = list(map(int,input().split()))
count = [0] * 11
triplet = 0
run = 0
for i in range(6):
    count[data[i]] +=1
for i in range(11):
    if count[i] >=3:
        triplet +=1
        count[i] -= 3
for i in range(8):
    if count[i+2]==1 and count[i+1] == 1 and count[i] ==1:
        run +=1
        count[i+2] -=1
        count[i+1] -=1
        count[i] -=1
if run==1 and triplet==1:
    print('babygin')
else:
    print('실패')