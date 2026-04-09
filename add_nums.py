from typing import List


def plusOne(digits: List[int], carry) -> List[int]:
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] + carry <= 9:
            digits[i] += carry
            break
        digits[i] += carry
        carry = digits[i] // 10
        digits[i] = digits[i] % 10

    if digits[0] == 0:
        return [1] + digits
    else:
        return digits

arr = [9,9,9,4]
carry = 7
print(plusOne(arr, carry))

