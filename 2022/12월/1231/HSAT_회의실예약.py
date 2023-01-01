# HSAT 회의실 예약
import sys

N,M = map(int,input().split())
room = {}
room_name = []
for i in range(N):
    name = input()
    room_name.append(name)
    room[name] = [0]*19


for i in range(M):
    a,b,c= input().split()
    b,c = int(b),int(c)
    for i in range(b,c+1):
        room[a][i] = 1
room_name.sort()
for i in room_name:
    room[i] = room[i][9:19]
time = []
for i in room_name:
    temp = []
    for j in range(11):
        if room[i][j]==0:
            temp.append(j+9)
    time.append(temp)
print(time)
# for i in range(len(room_name)-1):
#     if 0 not in room[room_name[i]]:
#         print(f'Room {room_name[i]}:')
#         print('Not available')
#     else:
#         print(f'Room {room_name[i]}:')
#         temp = []
#         for j in range(10):
#             if room[room_name[i]][j]==1:
#                 temp.append(j+9)
#         temp.sort()
#         print(temp)
#         for j in range(len(temp)-1):
#             print(temp[j+1],temp[j],temp[j+1]-temp[j])
#         print()
#     print('-----')
#
#
