blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']

blood_dict = {}

for blood in blood_types:
    if blood_dict.get(blood):
        blood_dict[blood] += 1
    else:
        blood_dict[blood] = 1

print(blood_dict)