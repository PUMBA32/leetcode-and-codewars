# 338

class Solution:
    @staticmethod
    def countBits(n: int) -> list[int]: 
        return [bin(i).count('1') for i in range(n+1)]


print(Solution.countBits(2))   # [0,1,1]
print(Solution.countBits(5))   # [0,1,1,2,1,2] 
        