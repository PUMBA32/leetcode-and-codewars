# 191

class Solution:
    @staticmethod
    def hammingWeight(n: int) -> int:
        bits = 0
        while n >= 1:
            if n % 2 == 1: bits += 1
            n //= 2
        return bits


print(Solution.hammingWeight(11))  # 3
print(Solution.hammingWeight(128))  # 1
print(Solution.hammingWeight(2147483645))  # 30