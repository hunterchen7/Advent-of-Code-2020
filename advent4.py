set1 = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

pprts = open('advent4.txt', 'r').readlines()
print(pprts)

all_ppts = []

curr_ppt = ''

for pprt in pprts:
    if pprt != '\n':
        curr_ppt += pprt
    else:
        print(curr_ppt)
        all_ppts.append([i[0:3] for i in curr_ppt.split()])
        curr_ppt = ''

print(all_ppts)

valid = 0 #sum([i == set1 or i == set2 for i in all_ppts])

for pprt in all_ppts:
    v = True
    for para in pprt:
        if para not in set1:
            v = False
    if v: valid += 1

print(valid)