def find_two_numbers(nums, target):
    set_nums = set(nums)
    for num in nums:
        if target - num in set_nums:
            return num * (target - num)

def find_three_numbers(nums, target):
    set_nums = set(nums)
    for num in nums:
        for num2 in nums:
            if (target - num - num2) in set_nums:
                return num * (target - num - num2) * num2

with open("day1/input.txt") as _file:
    nums = [int(line) for line in _file]

    p1 = find_two_numbers(nums, 2020)
    p2 = find_three_numbers(nums, 2020)

    print("Part 1:", p1)
    print("Part 2:", p2)