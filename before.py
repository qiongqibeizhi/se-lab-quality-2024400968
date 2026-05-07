

# 问题1：除零错误（Division by Zero）
def divide(a, b):
    result = a / b      # 当b=0时抛出ZeroDivisionError
    return result


# 问题2：未使用的变量（Unused Variable）
def calculate_price(price):
    tax_rate = 0.1      # 定义了但从未使用
    discount = 0.9
    return price * discount