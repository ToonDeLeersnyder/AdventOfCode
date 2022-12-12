
def meets_criteria_one(password, letter, start, stop):
    return password.count(letter) >= start and password.count(letter) <= stop

def meets_criteria_two(password, letter, start, stop):
    return (password[start] == letter or password[stop] == letter) and (password[start] != password[stop])

def count_passwords(passwords, criteria_function):
    count = 0
    for policy, password in passwords:
        length, letter = policy.split(" ")
        start, stop = length.split("-")
        start, stop = int(start), int(stop)

        if criteria_function(password, letter, start, stop):
            count += 1
    return count

with open('day2/input.txt') as file:
    letters = [num.split(": ") for num in file]

    # part 1
    p1 = count_passwords(letters, meets_criteria_one)
    print("Part 1:", p1)

    # part 2
    p2 = count_passwords(letters, meets_criteria_two)
    print("Part 2:", p2)