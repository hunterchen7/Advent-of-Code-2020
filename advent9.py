from itertools import combinations

nums = [int(i) for i in open('advent9.txt', 'r').readlines()]

print(list(combinations(nums[0:25], 2)))

def part1(nums):
    for num, j in zip(nums[25:], range(25,len(nums))):
        if num not in [sum(i) for i in list(combinations(nums[j-25:j], 2))]:
            return num

print(part1(nums))

target = part1(nums)

def part2(nums, target):
    for num_len in range(2, len(nums)):
        for i in range(0, len(nums) - num_len):
            #print(i, num_len, nums[i:num_len], end=' - ')
            contiguous = nums[i:num_len]
            if sum(contiguous) == target:
                return min(contiguous) + max(contiguous)

print(part2(nums, target))