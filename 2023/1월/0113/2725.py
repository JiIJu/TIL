# # 2725 보이는 점의 개수
# def gcd(a,b):
#     while b>0:
#         a,b = b,a%b
#     return a
# num = [0]*1001
# # num[1],num[2],num[3] = 3,5,9
# cnt = 0
# for i in range(1,1001):
#     for j in range(1,i+1):
#         if gcd(i,j)==1:
#             cnt+=1
#     num[i] = cnt
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     print(2*num[N]+1)
#
#
#

a = [1,2,3,4,5]
print(a[:-2])