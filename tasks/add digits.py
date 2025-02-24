# 258

class Solution:
    @staticmethod
    def addDigits(num: int) -> int:
        while len(str(num)) != 1:  
            num = sum(list(map(int, list(str(num)))))
        return num
    
    @staticmethod
    def addDigits2(num: int) -> int:
        while num >= 10:
            s = 0
            while num > 0:
                s += num % 10
                num //= 10
            num = s
        return num


print(Solution.addDigits2(38))  # 2
print(Solution.addDigits2(0))  # 0


