# calc.py - 存在CodeQL可检测的问题

# 问题1：未使用的导入
import math
import json

# 问题2：未使用的变量
UNUSED_CONSTANT = 3.14159
temp_value = 100

def add(a, b):
    return a + b

def add2(a, b):      # 与add重复
    return a + b

# 问题3：除零错误（CodeQL必报）
def divide(a, b):
    return a / b      # b可能为0

def calc_price(price):
    return price * 0.8  # 魔法数字