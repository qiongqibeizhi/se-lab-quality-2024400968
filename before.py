def calculate_total(price, count):
    tax = price * 0.13
    total = price + tax
    if count > 10:
        discount = total * 0.9
        return discount
    else:
        return total

def calculate_total_vip(price, count):
    tax = price * 0.13
    total = price + tax
    if count > 10:
        discount = total * 0.85
        return discount
    else:
        return total

unused_var = 100

print(calculate_total(100, 5))
print(calculate_total_vip(100, 15))