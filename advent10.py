adapters = [0] + sorted([int(i.strip()) for i in open('advent10.txt', 'r').readlines()])
print(adapters)


#advent10c.txt -> part B: 2^8 * 7^13

#example2 = [0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, 52]

#e1 = [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]

def part1(adapters):
    j1 = 1
    j3 = 1

    for v1, v2 in zip(adapters, adapters[1:]):
        v_diff = v2 - v1
        if v_diff == 3:
            j3 += 1
        elif v_diff == 1:
            j1 += 1
    print(len(adapters),j1,j3)
    return j1 * j3

def part2_spliter(adapters):
    split_adapters = []
    curr_list = [adapters[0]]

    for v1, v2 in zip(adapters, adapters[1:]):
        v_diff = v2 - v1
        if v_diff == 3:
            split_adapters.append(curr_list)
            curr_list = []
        curr_list.append(v2)

    split_adapters.append(curr_list)

    return split_adapters

#print(part1(adapters))

split_adapters = part2_spliter(adapters)

#print(split_adapters)

def part2(adapters):
    perms = 1
    # each segment must have end and beginning
    for a in adapters:
        if len(a) == 5:
            perms *= 7 # C(3,1) + C(3,2) + C(3,0) = 3 + 3 + 1 = 7
        elif len(a) == 4:
            perms *= 4 # C(2,0) + C(2,1) + C(2,2)  = 1 + 2 + 1 = 4
        elif len(a) == 3:
            perms *= 2 # C(1,0) + C(1,1) = 1 + 1 = 2
    return perms

#print(adapters)
print(split_adapters)
print(part2(split_adapters))