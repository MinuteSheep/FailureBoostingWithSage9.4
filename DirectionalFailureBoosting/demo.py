import math 

def decimal_to_power_of_2(decimal): 
    # 将小数转换为对数 
    log_value = math.log2(decimal) 
    # 将对数向上取整，得到最接近的2的次幂的指数 
    exponent = math.ceil(log_value) 
    # 计算得到最接近的2的次幂 
    result = 2 ** exponent 
    return result 

# 示例 
decimal = 0.75 
result = decimal_to_power_of_2(decimal) 
print(f"将小数 {decimal} 转换为最接近的2的次幂的形式为: {result}")

