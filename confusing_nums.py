# https://interviewing.io/questions/confusing-number

confusing_digits = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}


def is_confusing(num):
    flipped_num = 0
    orig = num
    while num > 0:
        if num % 10 in confusing_digits:
            flipped_num = flipped_num * 10 + confusing_digits[num%10]
            num = num // 10
        else:
            return False
    if orig == flipped_num or flipped_num > 800:
        return False
    else:
        return True


def get_confusing_nums():
    confusing_nums = []
    for i in range(800):
        if i % 10 == 0:
            continue
        if is_confusing(i):
            confusing_nums.append(i)
    return confusing_nums


print(get_confusing_nums())
print(len(get_confusing_nums()))


def find_confusable_numbers():
    flip_map = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

    def isConfusable(num):
        flipped = ""
        for digit in str(num):
            if digit not in flip_map:
                return False
            flipped += flip_map[digit]

        # Check if the flipped number is different from the original number
        if num != int(flipped):
            # Check if the flipped number ends in zero, which would make it invalid
            if flipped[-1] == "0":
                return False
            # Check if the first digit is 6 and the last digit is 9, or vice versa
            if (flipped[0] == "6" and flipped[-1] == "9") or (flipped[0] == "9" and flipped[-1] == "6"):
                return False
            # Check if the number is a three-digit number and satisfies the specific conditions
            if len(str(num)) == 3 and (num % 10 == 0 or num % 10 == 8 or num % 10 == 6):
                return False
            return True

        return False

    confusables = []
    for num in range(1, 800):
        if isConfusable(num):
            confusables.append(num)

    return confusables


confusables = find_confusable_numbers()
print(confusables)
