# 412

'''
Given an integer n, return a string array answer (1-indexed) where:

    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.

'''

class Solution:
    @staticmethod
    def fizzBuzz(n: int) -> list[str]:
        arr = []
        for el in range(1, n+1):
            arr.append(
                "FizzBuzz" if el % 3 == 0 and el % 5 == 0 else
                "Fizz" if el % 3 == 0 else
                "Buzz" if el % 5 == 0 else
                str(el)
            )
        return arr

print(Solution.fizzBuzz(3))  # ["1","2","Fizz"]
print(Solution.fizzBuzz(5))  # ["1","2","Fizz","4","Buzz"]
print(Solution.fizzBuzz(15))  # ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
        