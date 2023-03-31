def intToRoman(num: int) -> str:
    res = ""
    while num >= 1000:
        res += "M"
        num -= 1000
    while num >= 500:
        res += "D"
        num-=500
        if num >= 900:
            res = res[:-1]
            res += "CM"
            num -= 400
        elif num > 100:
            res += "C"
            num -= 100
    while num >= 100:
        if num >= 400:
            res += "CD"
            num -= 400
        else:
            res += "C"
            num -= 100
    while num >= 50:
        res += "L"
        num -= 50
        if num >= 40:
            res = res[:-1]
            res += "XC"
            num -= 40
        elif num > 10:
            res += "X"
            num -= 10
    while num >= 10:
        if num >= 40:
            res += "IV"
            num -= 40
        else:
            res += "X"
            num -= 10
    while num >= 5:
        res += "V"
        num -= 5
        if num >=4:
            res = res[:-1]
            res += "IX"
            num -= 4
        elif num > 1:
            res += "I"
            num -= 1
    while num > 0:
        if num == 4:
            res += "IV"
            num -= 4
        else:
            res += "I"
            num -= 1
    print(res)
    return res


intToRoman(58)
intToRoman(1994)