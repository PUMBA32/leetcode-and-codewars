'''Найти минимальное натуральное число, у которого сумма четырех натуральных делителей равна 2025'''


from typing import List, Optional

def get_factors(n: int, count: int = 1) -> Optional[List[int]]: 
    return [i for i in range(n, 0, -1) if n % i == 0][:count]

n: int = 1
while True:
    if (factors := get_factors(n, 4)) and (s := sum(factors)) == 2025: 
        print(f'{n}: {factors} -> {s}')
        break
    print(f'{n}: {factors} -> {s}')
    n += 1


'''Ответ: 927'''