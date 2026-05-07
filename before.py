# 坏味道1：重复代码
def validate_name(name):
    if len(name) < 3:
        return False
    if len(name) > 20:
        return False
    if not name.isalnum():
        return False
    return True

def validate_nickname(nickname):
    if len(nickname) < 3:
        return False
    if len(nickname) > 20:
        return False
    if not nickname.isalnum():
        return False
    return True

# 坏味道2：过长函数
def register_user(username, email, password, phone):
    # 验证用户名
    if len(username) < 3 or len(username) > 20:
        return "用户名长度错误"
    if not username.isalnum():
        return "用户名格式错误"
    
    # 验证邮箱
    if "@" not in email:
        return "邮箱格式错误"
    
    # 验证密码
    if len(password) < 8:
        return "密码长度不足"
    if not any(c.isupper() for c in password):
        return "密码需要大写字母"
    if not any(c.isdigit() for c in password):
        return "密码需要数字"
    
    # 验证手机
    if not phone.isdigit() or len(phone) != 11:
        return "手机号错误"
    
    return "注册成功"

# 坏味道3：未使用的变量
UNUSED = "这个变量没用"

def calc_discount(price, level):
    temp = 100  # 未使用
    x = 0       # 未使用
    if level == "gold":
        return price * 0.8
    elif level == "silver":
        return price * 0.9
    else:
        return price

# 坏味道4：深层嵌套
def check_book(book, user):
    if book is not None:
        if book.get("status") == "available":
            if user is not None:
                if user.get("verified"):
                    return True
    return False