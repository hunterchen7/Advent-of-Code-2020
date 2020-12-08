bags = {} #part1
numed_bags = {} #part2
import time
start = time.time()

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

bag_count = 0
bag_contain_count = {} # number of bags in each type of bag, including self

print(numed_bags)

for bag in numed_bags:
    if numed_bags[bag] == {}:
        bag_contain_count[bag] = 1

print(bag_contain_count)

while [i for i in bag_contain_count] != [i for i in numed_bags]:
    if time.time() - start > 25:
        break
    for bag in numed_bags:
        bag_content = [clr for clr in numed_bags[bag]]
        if sum([True if bag in bag_contain_count else False for bag in bag_content]) == len(bag_content) and bag not in bag_contain_count: #all of bag_content is in bag_contain_count
            inner_bags = []
            for inner_bag in bag_content:
                inner_bags.append(bag_contain_count[inner_bag] * numed_bags[bag][inner_bag])
            bag_contain_count[bag] = sum(inner_bags)

print(bag_contain_count)

print(bag_contain_count['shiny gold'])

#quite ugly but it is what it is. really gotta learn recursion :(