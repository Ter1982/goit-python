'''
def calculate_inflation(*month_inflation):
    y = len(month_inflation)
    for i in month_inflation:
        i *= i
    return i ** (1./y)

a =  calculate_inflation(1, 2, 3)
print(a)

'''
'''
def calculate_inflation(*month_inflation):
    y = len(month_inflation)
    i = 1
    for item in month_inflation:
        i *= item
    return i ** (1/y)
a =  calculate_inflation(1, 2, 3)
print(a)
'''
'''
def is_prime(n, d=3):
    if n % 2 != 0:
        return True
    if n % d == 0:
        return False
    if d * d > n:
        return True
    return is_prime(n, d + 1)



print(is_prime(4))
'''


def is_prime(n, d=3):
    if n == 1: return False 
    if n > d:       
        if n % d == 0:
            return False
        if d * d > n: 
            return True
    else: return True
    return is_prime(n, d + 1)  
print(is_prime(3))








