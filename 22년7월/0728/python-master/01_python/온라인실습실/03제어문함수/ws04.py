blood_types = ["A", "A", "O", "B", "A", "O", "AB", "O", "A", "B", "O", "B", "AB"]

blood_count = {}

for bt in blood_types:
    if bt not in blood_count.keys():
        blood_count.update({bt: 1})
    else:
        blood_count[bt] += 1

print(blood_count)
