bags = {} #part1
numed_bags = {} #part2

for bag in [i.strip('. \n').split('bag')[:-1] for i in open('advent7.txt', 'r').readlines()]: 
    main_bag = bag[0].strip()
    numed_bags[main_bag] = {}

    bags[main_bag] = [' '.join(clr.strip().split(' ')[-2:]) for clr in bag[1:]]
    for line in bag[1:]:
        line = line.strip().split(' ')[-3:]
        clr = ' '.join(line[-2:])
        if line[0] != 'contain':
            count = int(line[0])
            numed_bags[main_bag][clr] = count

def bag_types(bags):
    valid_bags1 = set()
    valid_bags2 = set()

    for bag in bags:
        if 'shiny gold' in bags[bag]:
            valid_bags1.add(bag)

    while valid_bags1 != valid_bags2:
        valid_bags2 = set(list(valid_bags1))

        for inner_bag in valid_bags1:
            for outer_bag in bags:
                if inner_bag in bags[outer_bag]:
                    valid_bags2.add(outer_bag)
        
        for inner_bag in valid_bags2:
            for outer_bag in bags:
                if inner_bag in bags[outer_bag]:
                    valid_bags1.add(outer_bag)

    return(valid_bags1)

valid_bags = bag_types(bags)
print(len(valid_bags))

def count_inner_bags(count_bag):
    total_bags = 0

    for inner_bag in bags[count_bag]:
        if numed_bags[count_bag] == {}:
            total_bags += 1
            return total_bags
        else:
            return numed_bags[count_bag][inner_bag] * count_inner_bags(inner_bag)

    return total_bags

print(count_inner_bags('shiny gold'))