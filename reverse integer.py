'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value 
to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

'''

def reverse_integer(x: int) -> int:
    if x == 0: return 0

    temp = "-" if x < 0 else "" 

    result = ""
    start_zero = True

    for s in str(x)[::-1].replace("-", ""):
        if s == '0' and start_zero: continue
        start_zero = False
        result += s
    
    res: int = int(temp+result)
    
    return res if -2**31 <= res <= 2**31-1 else 0 


def reverse_integer_2(x: int) -> int:
    res: int = 0

    while x != 0:
        res = res * 10 + x % 10
        x /= 10

    return res if -2**31 < res < 2**31-1 else 0 

            

print(reverse_integer_2(123))  # 321
print(reverse_integer_2(-123))  # -321
print(reverse_integer_2(120))  # 21
print(reverse_integer_2(0))  # -
print(reverse_integer_2(1))  # 1
print(reverse_integer_2(1534236469))  # 0
