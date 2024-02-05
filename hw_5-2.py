import re
from typing import Callable

text = '''Загальний дохід працівника складається з декількох 
частин: 1000.01 як основний дохід, доповнений додатковими 
надходженнями 27.45 і 324.00 доларів.'''

def generator_numbers(text: str):
    pattern=r'\d+\.\d+'
    numbers=re.findall(pattern,text)
    for num in numbers:
        num=float(num)
        yield num

for num in generator_numbers(text):
    print(num)

def sum_profit(text: str, generator_numbers: Callable):
    total_income=sum(generator_numbers)
    return total_income

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
