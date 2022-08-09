
density_brine_list = []

for i in range(5):
    density_brine = input('소금물의 농도(%)와 소금물의 양(g)을 입력하십시오 : ').split()

    if density_brine[0] == 'Done' or density_brine[1] == 'Done':
        break
    else:
        density_brine_list.append(density_brine)
salt = 0
for i in range(len(density_brine_list)):
    salt += float(density_brine_list[i][0]) * float(density_brine_list[i][1]) * 0.01

total_brine = 0
for i in range(len(density_brine_list)):
    total_brine += float(density_brine_list[i][1])
density = round(salt/total_brine * 100,2)
print(f'{density}% {total_brine}')