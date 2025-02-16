class Solution:
    @staticmethod
    def generate(nRows: int) -> list[list[int]]:
        res = []

        for r in range(1, nRows+1):
            res.append([1 if c == 1 or c == r else res[r-2][c-2]+res[r-2][c-1] 
                        for c in range(1, r+1)])           
        
        return res


print(Solution.generate(1), '\n')

print(Solution.generate(2), '\n')

print(Solution.generate(3), '\n')

print(Solution.generate(4), '\n')

print(Solution.generate(5), '\n')