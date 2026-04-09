def digit_product(num):
    product = 1
    while num > 0:
        product = product * (num % 10)
        print(num % 10, num // 10, product)
        num = num // 10
    return product

digit_product(25)