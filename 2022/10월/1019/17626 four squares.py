# # def comb():
# #     for i in range(1<<int(n**0.5)):
# #         res = []
# #         for j in range(int(n**0.5)):
# #             if len(res)<5 and sum(res)<=n:
# #                 if i & (1<<j):
# #                     res.append(data[j])
# #         if res not in ans and len(res)<=4 and sum(res)==n:
# #             ans.append(res)
# n = int(input())
#
# data = [0]*50001
# for i in range(1,n+1):
#     ans = []
#     j = 1
#     while i>=j**2:
#         ans.append(data[i-j**2])
#         j+=1
#     data[i] = min(ans)+1
#
# print(data[n])
#
#
#

