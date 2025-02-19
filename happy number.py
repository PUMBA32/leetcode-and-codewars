class Solution:
    @staticmethod
    def isHappy(n: int) -> bool:

        while True:
            arr_n = list(map(int, str(n)))
            n = sum([a**2 for a in arr_n])
            print(n)
            if 1 < n < 10 and n != 7: return False 
            if n == 1: return True
    
# print(Solution.isHappy(19))
# print(Solution.isHappy(20))
# print(Solution.isHappy(21))
#print(Solution.isHappy(7))
print(Solution.isHappy(1111111))
